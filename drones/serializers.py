from abc import ABC

from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from drones.models import Drone, MedicinesLoadedByDrones, OPTION_CHOICE_STATE_LOADED
from drones.validator import validate_loading_medications
from medications.models import Medication


class DroneSerializer(ModelSerializer):
    """
    Drone Serializer
    """

    class Meta:
        """
        Class Meta
        """
        model = Drone
        exclude = ("state",)


class MedicinesLoadedByDronesSerializer(Serializer):
    """
    MedicinesLoadedByDrones Serializer
    """
    drone = PrimaryKeyRelatedField(queryset=Drone.objects.all())
    medications = ListField(child=PrimaryKeyRelatedField(queryset=Medication.objects.all()), min_length=1)

    @transaction.atomic
    def create(self, validated_data):
        """

        :param validated_data:
        :return:
        """
        drone = validated_data.get('drone')
        for medication in validated_data.get('medications'):
            MedicinesLoadedByDrones.objects.create(
                drone=drone,
                medication=medication
            )

        drone.state = OPTION_CHOICE_STATE_LOADED
        drone.save()

        return Drone
