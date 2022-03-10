import re

from django.core.exceptions import ValidationError


def validate_name(value):
    """

    :param value:
    :return:
    """
    regex = '^([a-zA-Z0-9])+([a-zA-Z0-9]|((\_|\-)[a-zA-Z0-9]))*$'
    if not re.fullmatch(regex, value):
        raise ValidationError('Incorrect format.', params={'value': value})


def validate_code(value):
    """

    :param value:
    :return:
    """
    regex = '([A-Z0-9])+([A-Z0-9]|(\_[A-Z0-9]))*'
    if not re.fullmatch(regex, value):
        raise ValidationError('Incorrect format.', params={'value': value})
