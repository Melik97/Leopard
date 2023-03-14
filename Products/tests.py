from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class testCreateCategories(APITestCase):

    def authenticate(self):
        user = {
            'email': 'user1@gmail.com',
            'password': '123456',
            'full_name': 'user1',
            'phone_number': '09210863056',
            }
        self.client.post(reverse('register-users'), user)
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'email': user['email'], 'password': user['password']})
        self.client.credentials(
            HTTP_AUTHORIZATION=f'bearer {response.data["token"]}'
            )

    def test_create_categories(self):
        sample_test = {'title': "Heloo", "desc": "ok"}
        response = self.client.post(reverse('categories'), sample_test)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
