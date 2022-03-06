from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drones.models import Drone, MedicinesLoadedByDrones
from drones.serializers import DroneSerializer, MedicinesLoadedByDronesSerializer


class CreateDroneView(GenericViewSet, CreateAPIView):
    """
    Create Drone
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


create_drone_view = CreateDroneView


class CreateMedicinesLoadedByDroneView(GenericViewSet, CreateAPIView):
    """
    Create MedicinesLoadedByDrone
    """
    queryset = Drone.objects.all()
    serializer_class = MedicinesLoadedByDronesSerializer

    def create(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {
            'message': 'Successfully loaded drone'
        }
        return Response(response, status=status.HTTP_201_CREATED)


create_medicines_loaded_by_drone_view = CreateMedicinesLoadedByDroneView
