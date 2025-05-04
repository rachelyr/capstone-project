from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import generics
from .models import Menu, BookingTable
from .serializers import MenuSerializer, BookingTableSerializer

# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
    #permission_classes = [permissions.isAuthenticated]