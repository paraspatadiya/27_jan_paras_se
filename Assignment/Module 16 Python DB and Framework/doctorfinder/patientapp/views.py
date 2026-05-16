from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from . models import *
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from . forms import *
from adminapp.models import doctor
from django.conf import settings

# Create your views here.
def home(request):
    if not request.user.is_authenticated and 'user' not in request.session:
        return redirect('/')

    user = request.user.username if request.user.is_authenticated else request.session.get('user')
    return render(request, 'home.html', {'user': user})

def login(request):
    if request.method == 'POST':
        unm = request.POST['email']
        pas = request.POST['password']

        # Try standard Django auth first (for social/migrated users)
        user = authenticate(username=unm, password=pas)
        if user is not None:
            auth_login(request, user)
            return redirect('/home/')

        # Fallback to legacy custom auth
        legacy_user = patientsignup.objects.filter(email=unm, password=pas).first()
        if legacy_user:
            # Ensure a Django User exists and link it
            if not legacy_user.user:
                dj_user = User.objects.filter(email=legacy_user.email).first()
                if not dj_user:
                    # Create a new Django user for the legacy patient
                    dj_user = User.objects.create_user(username=legacy_user.email, email=legacy_user.email, password=legacy_user.password)
                legacy_user.user = dj_user
                legacy_user.save()
            
            # Log in the user to standard Django auth
            auth_login(request, legacy_user.user)
            
            request.session['user'] = unm
            request.session['userid'] = legacy_user.id
            return redirect('/home/')
        else:
            print("Error! Login failed...")

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save to custom model
            p_signup = form.save()
            
            # Also create a Django User for social/standard auth compatibility
            user = User.objects.create_user(username=p_signup.email, email=p_signup.email, password=p_signup.password)
            p_signup.user = user
            p_signup.save()
            
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'signup.html')

def userlogout(request):
    logout(request)
    request.session.flush()
    return redirect('/')

def profile(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile = patientsignup.objects.filter(user=request.user).first()
        if not user_profile:
            user_profile = patientsignup.objects.filter(email=request.user.email).first()
    
    if not user_profile and 'userid' in request.session:
        user_profile = patientsignup.objects.filter(id=request.session['userid']).first()

    if not user_profile:
        messages.error(request, "Could not find your profile details. Please log in again.")
        return redirect('/home/')

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('/profile/')
    else:
        form = UpdateForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})

def doctors(request):
    query = request.GET.get('q')
    if query:
        data = doctor.objects.filter(specialization__icontains=query)
    else:
        data = doctor.objects.all()
    return render(request, 'doctors.html', {'data': data})

def about(request):
    return render(request, 'about.html')

def book_appointment(request, doctor_id):
    if not request.user.is_authenticated and 'user' not in request.session:
        return redirect('/')
    
    doc = doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        # Use authenticated user if available, otherwise fallback and ensure link
        if request.user.is_authenticated:
            user = request.user
        else:
            p_profile = patientsignup.objects.get(id=request.session['userid'])
            if not p_profile.user:
                # Emergency fallback: create user if missing
                dj_user = User.objects.filter(email=p_profile.email).first()
                if not dj_user:
                    dj_user = User.objects.create_user(username=p_profile.email, email=p_profile.email, password=p_profile.password)
                p_profile.user = dj_user
                p_profile.save()
            user = p_profile.user
            
        try:
            appointment = Appointment.objects.create(
                patient=user,
                doctor=doc,
                date=date,
                time=time,
                status='Booked'
            )
            return redirect('booking_success', appointment_id=appointment.id)
        except Exception as e:
            print(f"Appointment Creation Error: {e}")
            return render(request, 'book_appointment.html', {
                'doctor': doc, 
                'error': "Booking failed due to an internal error. Please contact support."
            })
        
    return render(request, 'book_appointment.html', {'doctor': doc})

def booking_success(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'booking_success.html', {'appointment': appointment})