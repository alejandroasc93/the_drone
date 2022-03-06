from rest_framework.serializers import ModelSerializer

from drones.models import Drone


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
