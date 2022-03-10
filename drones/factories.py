from factory.django import DjangoModelFactory

from drones.models import Drone


class DroneFactory(DjangoModelFactory):
    """
    Drone factory
    """
    class Meta:
        """
        Class Meta
        """
        model = Drone

