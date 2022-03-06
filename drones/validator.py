from django.core.exceptions import ValidationError as ValidationErrorRestFramework
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from medications.models import Medication


def validate_max_weight(value):
    """

    :param value:
    :return:
    """
    if value > 500:
        raise ValidationError(_("The weight cannot be more than 500gr."))


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
