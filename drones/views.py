from django.core.exceptions import BadRequest
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from drones.models import Drone, OPTION_CHOICE_STATE_IDLE, OPTION_CHOICE_STATE_LOADED
from drones.serializers import DroneSerializer, MedicinesLoadedByDronesSerializer, CheckingLoadedMedicationSerializer, \
    BatteryLevelDroneSerializer


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


class CheckingLoadedMedicationView(ModelViewSet, RetrieveAPIView):
    """
    CheckingLoadedMedication View
    """
    queryset = Drone.objects.all()
    serializer_class = CheckingLoadedMedicationSerializer

    def retrieve(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        if instance.state != OPTION_CHOICE_STATE_LOADED:
            return Response({'message': 'The drone is not in loaded status'}, HTTP_400_BAD_REQUEST)
        return super(CheckingLoadedMedicationView, self).retrieve(request, *args, **kwargs)


checking_loaded_medication_view = CheckingLoadedMedicationView


class CheckingAvailableDronesView(GenericViewSet, ListAPIView):
    """
    CheckingAvailableDrones View
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer

    def filter_queryset(self, queryset):
        """

        :param queryset:
        :return:
        """
        queryset = super(CheckingAvailableDronesView, self).filter_queryset(queryset)
        return queryset.filter(battery_capacity__gt=25, state=OPTION_CHOICE_STATE_IDLE)


checking_available_drone_view = CheckingAvailableDronesView


class CheckingBatteryLevelView(GenericViewSet, RetrieveAPIView):
    """
    CheckingBatteryLevel View
    """
    queryset = Drone.objects.all()
    serializer_class = BatteryLevelDroneSerializer


checking_battery_level_view = CheckingBatteryLevelView
