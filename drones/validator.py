from django.core.exceptions import ValidationError as ValidationErrorRestFramework
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from medications.models import Medication


def validate_max_weight(value):
    """

    :param value:
    :return:
    """
    if 0 > value > 500:
        raise ValidationError(_("The weight cannot be greater than 500gr and less than 0gr."))


def validate_battery_capacity(value):
    """

    :param value:
    :return:
    """
    if 0 > value > 100:
        raise ValidationError(_("The battery capacity cannot be greater than 100% and less than 0%."))


def validate_loading_medications(drone, medications):
    """

    :param drone:
    :param medications:
    :return:
    """
    total = 0
    for medication in medications:
        total += medication.weight
        if total > drone.weight_limit:
            raise ValidationErrorRestFramework(
                'The total weight of the medications exceeds the weight limit of the drone')
