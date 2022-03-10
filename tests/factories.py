import factory

from drones.models import Drone, OPTION_CHOICE_MODEL_LIGHTWEIGHT
from medications.models import Medication


class DroneFactory(factory.Factory):
    """
    Drone Factory
    """
    class Meta:
        """
        Class Meta
        """
        model = Drone

    serial_number = 'S999999'
    model = OPTION_CHOICE_MODEL_LIGHTWEIGHT
    weight_limit = 200


class MedicationFactory(factory.Factory):
    """
    Medication Factory
    """
    class Meta:
        """
        Class MEta
        """
        model = Medication

    name = 'Ozempic'
    code = '123456,'
    weight = 222
    image = '/image/medications.jpg'
