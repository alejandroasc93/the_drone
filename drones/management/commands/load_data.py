from random import randint

from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import transaction
from django.core.management.base import BaseCommand
from rest_framework.fields import ImageField

from drones.factories import DroneFactory
from drones.models import Drone, CHOICE_MODEL, CHOICE_STATE
from medications.factories import MedicationFactory
from medications.models import Medication
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

NUM_DRONES = 10
NUM_MEDICATION = 13

list_medication = [
    'Ozempic',
    'Pantoprazole',
    'Prednisone',
    'Probuphine',
    'Rybelsus',
    'secukinumab',
    'Sublocade',
    'Tramadol',
    'Trazodone',
    'Viagra',
    'Wellbutrin',
    'Xanax',
    'Zubsolv',
]

drone_model = [item[0] for item in CHOICE_MODEL]
state_model = [item[0] for item in CHOICE_STATE]


class Command(BaseCommand):
    """
    Command Load Data
    """
    help = "Generate data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Drone, Medication]

        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for i in range(0, NUM_DRONES):
            DroneFactory(
                serial_number=f"S{randint(11111, 99999)}",
                model=drone_model[randint(0, len(drone_model) - 1)],
                weight_limit=randint(1, 500),
                battery_capacity=randint(1, 100),
                state=state_model[randint(0, len(state_model) - 1)],
            )

        for i in range(0, NUM_MEDICATION):
            MedicationFactory(
                name=list_medication[randint(0, len(list_medication) - 1)],
                weight=randint(1, 500),
                code=randint(1, 100),
                image='/image/medications.jpg',
            )
