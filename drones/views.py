from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from drones.models import Drone
from drones.serializers import DroneSerializer, MedicinesLoadedByDronesSerializer, CheckingLoadedMedicationSerializer


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


class CheckingLoadedMedicationView(ModelViewSet):
    """
    CheckingLoadedMedication View
    """
    queryset = Drone.objects.all()
    serializer_class = CheckingLoadedMedicationSerializer

    @action(detail=True, methods=['post'])
    def checking(self, request, pk=None):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        response = {
            'message': 'Drone ready to loading.'
        }
        return Response(response, status=status.HTTP_201_CREATED)


checking_loaded_medication_view = CheckingLoadedMedicationView
