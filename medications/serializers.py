from rest_framework.serializers import ModelSerializer

from medications.models import Medication


class MedicationSerializer(ModelSerializer):
    """
    Medication Serializer
    """

    class Meta:
        """
        Class Meta
        """
        model = Medication
        fields = '__all__'
