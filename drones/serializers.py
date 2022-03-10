from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ListField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from drones.models import Drone, MedicinesLoadedByDrones, OPTION_CHOICE_STATE_LOADED, OPTION_CHOICE_STATE_LOADING, \
    OPTION_CHOICE_STATE_IDLE
from drones.validator import validate_loading_medications
from medications.models import Medication
from medications.serializers import MedicationSerializer


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

    def validate(self, attrs):
        """

        :param attrs:
        :return:
        """
        values = super(MedicinesLoadedByDronesSerializer, self).validate(attrs)
        drone = values.get('drone')
        validate_loading_medications(drone, values.get('medications'))

        if drone.state != OPTION_CHOICE_STATE_LOADING:
            raise ValidationError("The drone is not in loading status.")

        return values

    @staticmethod
    def validate_drone(value):
        """

        :param value:
        :return:
        """
        if value.battery_capacity < 25:
            raise ValidationError("The battery of the drone cannot be below 25%.")
        return value

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


class CheckingLoadedMedicationSerializer(ModelSerializer):
    """
    MedicinesLoadedByDrones Serializer
    """
    medications = MedicationSerializer(source='get_loaded_medications', many=True)

    class Meta:
        """
        Class Meta
        """
        model = Drone
        fields = ('id', 'medications')


class BatteryLevelDroneSerializer(ModelSerializer):
    """
    Battery Level Drone Serializer
    """

    class Meta:
        """
        Class Meta
        """
        model = Drone
        fields = ("id", "battery_capacity")
