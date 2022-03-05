from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from medications.utils import upload_medication_imagen
from medications.validator import validate_name, validate_code


class Medication(models.Model):
    """
    Medication model
    """
    name = models.CharField(_("Name"), max_length=255, validators=[validate_name])
    weight = models.FloatField(_("Weight"))
    code = models.CharField(_("Code"), max_length=255, validators=[validate_code])
    image = models.ImageField(_("Image"), upload_to=upload_medication_imagen)

    class Meta:
        db_table = "tbl_medication"
        verbose_name = "Medication"
        verbose_name_plural = "Medications"

    def __str__(self):
        return self.name
