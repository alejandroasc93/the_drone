from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from drones.models import Drone
from drones.serializers import DroneSerializer


class CreateDroneView(GenericViewSet, CreateAPIView):
    """
    Create Drone
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


create_drone_view = CreateDroneView
