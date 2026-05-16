import urllib.request
import urllib.parse
import json
import requests

from django.shortcuts import render, redirect
from django.contrib import messages
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- EXISTING VIEWS (PRESERVED) ---

def index(request):
    weather = None
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            api_key = 'ee1d866378c3b46e4ea7eac5246684ac'
            city_quoted = urllib.parse.quote(city)
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city_quoted}&APPID={api_key}&units=metric'
            try:
                req = urllib.request.Request(url)
                with urllib.request.urlopen(req) as response:
                    if response.status == 200:
                        data = json.loads(response.read().decode())
                        main_condition = data['weather'][0]['main'].lower()
                        desc = data['weather'][0]['description'].lower()
                        
                        if 'heavy' in desc:
                            condition_class = f"heavy-{main_condition}"
                        else:
                            condition_class = main_condition

                        weather = {
                            'city': data['name'],
                            'temperature': data['main']['temp'],
                            'feels_like': data['main']['feels_like'],
                            'pressure': data['main']['pressure'],
                            'description': data['weather'][0]['description'].capitalize(),
                            'icon': data['weather'][0]['icon'],
                            'humidity': data['main']['humidity'],
                            'wind_speed': data['wind']['speed'],
                            'main': condition_class,
                        }
            except Exception as e:
                pass

    stdata = docinfo.objects.all()
    return render(request, 'index.html', {'data': stdata, 'weather': weather})


@api_view(['GET'])
def getall(request):
    stdata = docinfo.objects.all()
    serial = DocSerial(stdata, many=True)
    return Response(serial.data)

@api_view(['GET'])
def getid(request, id):
    try:
        stid = docinfo.objects.get(id=id)
    except docinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial = DocSerial(stid)
    return Response(serial.data)
        
@api_view(['DELETE', 'GET'])
def deleteid(request, id):
    try:
        stid = docinfo.objects.get(id=id)
    except docinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serial = DocSerial(stid)
        return Response(serial.data)
    if request.method == 'DELETE':
        stid.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PUT', 'GET'])
def updateid(request, id):
    try:
        stid = docinfo.objects.get(id=id)
    except docinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = DocSerial(stid)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = DocSerial(stid, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def adddoctor(request):
    serial = DocSerial(data=request.data)
    if serial.is_valid():
        serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)
    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

# --- NEW TOOL VIEWS ---

def get_coordinates(request):
    """Instant Geocoding Redirect to Google Maps"""
    if request.method == 'POST':
        address = request.POST.get('address')
        if address:
            google_maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(address)}"
            return redirect(google_maps_url)
            
    return render(request, 'maps.html')


def github_tools(request):
    """GitHub Repo Lister & Creator"""
    repos = []
    created_repo = None
    
    if request.method == 'POST':
        action = request.POST.get('action')
        token = 'YOUR_GITHUB_PERSONAL_ACCESS_TOKEN' # User must provide this
        headers = {'Authorization': f'token {token}'}

        if action == 'list':
            username = request.POST.get('username')
            url = f"https://api.github.com/users/{username}/repos"
            res = requests.get(url)
            if res.status_code == 200:
                repos = res.json()
            else:
                messages.error(request, "User not found or API limit reached")

        elif action == 'create':
            repo_name = request.POST.get('repo_name')
            url = "https://api.github.com/user/repos"
            data = {'name': repo_name, 'private': False}
            res = requests.post(url, headers=headers, json=data)
            if res.status_code == 201:
                created_repo = res.json()
                messages.success(request, f"Repository '{repo_name}' created successfully!")
            else:
                messages.error(request, "Creation failed (Check Token)")

    return render(request, 'github.html', {'repos': repos, 'created_repo': created_repo})


def twitter_feed(request):
    """Fetch latest 5 public tweets using a free, public RSS bridge (Nitter)"""
    tweets = []
    if request.method == 'POST':
        username = request.POST.get('username', '').strip().replace('@', '')
        # Using a public Nitter instance as a free API bridge
        url = f"https://nitter.net/{username}/rss"
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(res.content)
                # Parse RSS items
                for item in root.findall('.//item')[:5]:
                    tweets.append({
                        'text': item.find('title').text,
                        'date': item.find('pubDate').text,
                        'link': item.find('link').text
                    })
            else:
                messages.error(request, "Public feed not found for this user (or Nitter instance is down).")
        except Exception as e:
            messages.error(request, "Unable to reach public social feed.")

    return render(request, 'twitter.html', {'tweets': tweets})


def country_info(request):
    """REST Countries API Tool"""
    country_data = None
    if request.method == 'POST':
        name = request.POST.get('country_name')
        url = f"https://restcountries.com/v3.1/name/{name}?fullText=true"
        try:
            res = requests.get(url).json()
            if isinstance(res, list):
                c = res[0]
                country_data = {
                    'name': c['name']['common'],
                    'population': c.get('population'),
                    'languages': ", ".join(c.get('languages', {}).values()),
                    'currencies': ", ".join([v['name'] for v in c.get('currencies', {}).values()]),
                    'flag': c['flags']['png'],
                    'capital': c.get('capital', ["N/A"])[0]
                }
            else:
                messages.error(request, "Country not found")
        except:
            messages.error(request, "Connection Error")

    return render(request, 'countries.html', {'country': country_data})





def calculate_distance(request):
    """Instant Redirect to Google Maps Directions"""
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        if origin and destination:
            google_maps_url = f"https://www.google.com/maps/dir/?api=1&origin={urllib.parse.quote(origin)}&destination={urllib.parse.quote(destination)}&travelmode=driving"
            return redirect(google_maps_url)

    return render(request, 'distance.html')


def doctor_map(request):
    """Instant Redirect to Google Maps for local Doctors"""
    city = request.GET.get('city', '')
    if city:
        query = f"doctors in {city}"
        google_maps_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(query)}"
        return redirect(google_maps_url)

    return render(request, 'doctor_locations.html', {'city': city})
