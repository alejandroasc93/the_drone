from factory.django import DjangoModelFactory

from medications.models import Medication


class MedicationFactory(DjangoModelFactory):
    """
    Drone factory
    """

    class Meta:
        """
        Class Meta
        """
        model = Medication
