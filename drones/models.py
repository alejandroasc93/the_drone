from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from drones.validator import validate_max_weight

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
    battery_capacity = models.IntegerField(_("Battery capacity"), default=100)
    state = models.CharField(_("State"), choices=CHOICE_STATE, max_length=25, default=OPTION_CHOICE_STATE_IDLE)

    class Meta:
        db_table = "tbl_drone"
        verbose_name = "Drone"
        verbose_name_plural = "Drones"

    def __str__(self):
        return self.serial_number
