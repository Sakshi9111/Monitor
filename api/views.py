from django.http import HttpResponse
from django.shortcuts import render
import imp
from pickle import TRUE
import re
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data["person"],many=TRUE)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def monitor(request):
    return render(request,'base/home.html')