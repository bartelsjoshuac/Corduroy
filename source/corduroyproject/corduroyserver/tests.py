from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Reports
from .models import Trails

def test_get_report(self):
    report = Trails.objects.create(name='Owl Creek Road', groomer='Mr Plow', report="Excellant")
    response = self.client.get(f'/dogs/{report.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Owl Creek Road'
                     
def test_get_trail(self):
    report = Trails.objects.create(name='Shrine Pass', location='Front Range', rating=10)
    response = self.client.get(f'/dogs/{trail.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], 'Shrine Pass'
                     
###  Need to finish this when I am done messing with the code and the update is working again