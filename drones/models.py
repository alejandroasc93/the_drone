from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

# Create your models here.
from drones.validator import validate_max_weight, validate_battery_capacity
from medications.models import Medication

OPTION_CHOICE_MODEL_LIGHTWEIGHT = "Lightweight"
OPTION_CHOICE_MODEL_MIDDLEWEIGHT = "Middleweight"
OPTION_CHOICE_MODEL_CRUISERWEIGHT = "Cruiserweight"
OPTION_CHOICE_MODEL_HEAVYWEIGHT = "Heavyweight"

CHOICE_MODEL = (
    (OPTION_CHOICE_MODEL_LIGHTWEIGHT, OPTION_CHOICE_MODEL_HEAVYWEIGHT),
    (OPTION_CHOICE_MODEL_MIDDLEWEIGHT, OPTION_CHOICE_MODEL_MIDDLEWEIGHT),
    (OPTION_CHOICE_MODEL_CRUISERWEIGHT, OPTION_CHOICE_MODEL_CRUISERWEIGHT),
    (OPTION_CHOICE_MODEL_HEAVYWEIGHT, OPTION_CHOICE_MODEL_HEAVYWEIGHT),
)

OPTION_CHOICE_STATE_IDLE = "IDLE"
OPTION_CHOICE_STATE_LOADING = "LOADING"
OPTION_CHOICE_STATE_LOADED = "LOADED"
OPTION_CHOICE_STATE_DELIVERING = "DELIVERING"
OPTION_CHOICE_STATE_DELIVERED = "DELIVERED"
OPTION_CHOICE_STATE_RETURNING = "RETURNING"

CHOICE_STATE = (
    (OPTION_CHOICE_STATE_IDLE, OPTION_CHOICE_STATE_IDLE),
    (OPTION_CHOICE_STATE_LOADING, OPTION_CHOICE_STATE_LOADING),
    (OPTION_CHOICE_STATE_LOADED, OPTION_CHOICE_STATE_LOADED),
    (OPTION_CHOICE_STATE_DELIVERING, OPTION_CHOICE_STATE_DELIVERING),
    (OPTION_CHOICE_STATE_DELIVERED, OPTION_CHOICE_STATE_DELIVERED),
    (OPTION_CHOICE_STATE_RETURNING, OPTION_CHOICE_STATE_RETURNING),
)


class Drone(models.Model):
    """
    Drone model
    """
    serial_number = models.CharField(_("Serial number"), max_length=100)
    model = models.CharField(_("Model"), choices=CHOICE_MODEL, max_length=25)
    weight_limit = models.FloatField(_("Weight limit"), validators=[validate_max_weight])
    battery_capacity = models.IntegerField(_("Battery capacity"), default=100, validators=[validate_battery_capacity])
    state = models.CharField(_("State"), choices=CHOICE_STATE, max_length=25, default=OPTION_CHOICE_STATE_IDLE)

    class Meta:
        db_table = "tbl_drone"
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return self.serial_number


class MedicinesLoadedByDrones(models.Model):
    """
    MedicinesLoadedByDrones model
    """
    drone = models.ForeignKey(Drone, verbose_name='drone', on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, verbose_name='medication', on_delete=models.CASCADE)
    load_date = models.DateTimeField(_("Load date"), auto_now_add=True, )
    delivery_date = models.DateTimeField(_("Delivery date"), null=True, blank=True)

    class Meta:
        db_table = "tbl_medicines_loaded_by_drones"
        verbose_name = "MedicinesLoadedByDrone"
        verbose_name_plural = "MedicinesLoadedByDrones"

    def __str__(self):
        return f"{self.drone} -- {self.medication}"


class HistoryBatteryLevel(models.Model):
    """
    HistoryBatteryLevel model
    """
    drone = models.ForeignKey(Drone, verbose_name='drone', on_delete=models.CASCADE)
    battery = models.IntegerField(_("Battery capacity"), default=100)
    date = models.DateTimeField(_("Date"), auto_now_add=True)

    class Meta:
        db_table = "tbl_history_battery_level"
        verbose_name = "HistoryBatteryLevel"
        verbose_name_plural = "HistoryBatteryLevels"

    def __str__(self):
        return f"{self.drone.serial_number}, {self.battery}%"
