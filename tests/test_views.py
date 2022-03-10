from django.test import TestCase
from drones.models import Drone, OPTION_CHOICE_MODEL_LIGHTWEIGHT, OPTION_CHOICE_STATE_LOADING
from medications.models import Medication


class ViewsTest(TestCase):
    register_drone_data = {
        "serial_number": "serial_number",
        "model": OPTION_CHOICE_MODEL_LIGHTWEIGHT,
        "weight_limit": 145
    }

    def setUp(self):
        """
        Set Up
        :return:
        """
        self.drone = Drone.objects.create(serial_number='S999999', model=OPTION_CHOICE_MODEL_LIGHTWEIGHT,
                                          weight_limit=300,state=OPTION_CHOICE_STATE_LOADING)
        self.medication = Medication.objects.create(name='Acetaminophen', code='C9999', weight=100)
        self.drone_load_medication_data = {
            "drone": self.drone.id,
            "medications": [self.medication.id]
        }

    def test_register_drone(self):
        response = self.client.post('/api/drone/create/', follow=True, data=self.register_drone_data)
        self.assertEqual(response.status_code, 201)

    def test_load_medication(self):
        response = self.client.post('/api/drone/load-medication/', data=self.drone_load_medication_data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_list_drone_medications(self):
        response = self.client.get(f'/api/drone/checking-loaded/{self.drone.id}/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_available_drones(self):
        response = self.client.get('/api/drone/checking-available/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_drone_battery(self):
        response = self.client.get(f'/api/drone/checking-battery-level/{self.drone.id}/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
