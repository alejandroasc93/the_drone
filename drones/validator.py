from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_max_weight(value):
    """

    :param value:
    :return:
    """
    if value > 500:
        raise ValidationError(_("The weight cannot be more than 500gr."), params={'value': value})
