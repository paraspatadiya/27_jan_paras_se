from urllib import request

from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    stdata=Studinfo.objects.all()
    cdata=Course.objects.all()
    return render(request,'index.html',{'data':stdata, 'cdata':cdata})

@api_view(['GET'])
def getall(request):
    stdata=Studinfo.objects.all()
    serial=StudSerial(stdata,many=True)
    return Response(serial.data)


@api_view(['GET'])
def getid(request,id):
    try:
        stid=Studinfo.objects.get(id=id)
    except Studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=StudSerial(stid)
    return Response(serial.data)
        
@api_view(['DELETE','GET'])
def deleteid(request,id):
    try:
        stid=Studinfo.objects.get(id=id)
    except Studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=StudSerial(stid)
        return Response(serial.data)
    if request.method=='DELETE':
        Studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['PUT','GET'])
def updateid(request,id):
    try:
        stid=Studinfo.objects.get(id=id)
    except Studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=StudSerial(stid)
        return Response(serial.data)

    if request.method=='PUT':
        serial=StudSerial(stid,data=request.data)

        if serial.is_valid():
            serial.save()
            return Response(serial.data)

        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addstudent(request):
    serial = StudSerial(data=request.data)

    if serial.is_valid():
        serial.save()
        return Response(serial.data, status=status.HTTP_201_CREATED)

    return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getcourse(request):
    cdata=Course.objects.all()
    serial=CourseSerial(cdata,many=True)
    return Response(serial.data)


@api_view(['GET'])
def getcourseid(request,id):
    try:
        cid=Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serial=CourseSerial(cid)
    return Response(serial.data)


@api_view(['POST'])
def addcourse(request):
    serial=CourseSerial(data=request.data)

    if serial.is_valid():
        serial.save()
        return Response(serial.data,status=status.HTTP_201_CREATED)

    return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','GET'])
def updatecourse(request,id):
    try:
        cid=Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=CourseSerial(cid)
        return Response(serial.data)

    if request.method=='PUT':
        serial=CourseSerial(cid,data=request.data)

        if serial.is_valid():
            serial.save()
            return Response(serial.data)

        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE','GET'])
def deletecourse(request,id):
    try:
        cid=Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=CourseSerial(cid)
        return Response(serial.data)

    if request.method=='DELETE':
        Course.delete(cid)
        return Response(status=status.HTTP_202_ACCEPTED)