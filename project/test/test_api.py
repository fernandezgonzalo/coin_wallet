from django.contrib.auth.models import User
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from gualet.models import User, Gualet, Transaction


class UserResourceTest(ResourceTestCaseMixin, TestCase):
    fixtures = ['auth', 'gualet']

    def test_user_create(self):
        data = {
            "username": "tintin",
            "email": "tintin@gmail.com",
            "password": "admin123",
            "first_name": "tintin",
            "last_name": "tintin"
        }
        resp = self.api_client.post('/api/v1/users/', format="json", data=data)
        self.assertHttpCreated(resp)


class GualetResourceTest(ResourceTestCaseMixin, TestCase):
    fixtures = ['auth', 'gualet']

    def test_gualet_create(self):
        data = {
            "label": "gualet x",
            "balance": 10000,
            "user": "/api/v1/users/1/"
        }
        resp = self.api_client.post(
            '/api/v1/gualets/',
            format="json",
            data=data
        )
        self.assertHttpCreated(resp)


class TransactionResourceTest(ResourceTestCaseMixin, TestCase):
    fixtures = ['auth', 'gualet']

    def test_transaction_create(self):
        old_amount_gualet_1 = Gualet.objects.get(id=1).balance
        old_amount_gualet_3 = Gualet.objects.get(id=3).balance

        data = {
            "address_from": "/api/v1/gualets/1/",
            "address_to": "/api/v1/gualets/3/",
            "amount": 1
        }
        resp = self.api_client.post(
            '/api/v1/transactions/',
            format="json",
            data=data
        )
        self.assertHttpCreated(resp)

        new_amount_gualet_1 = Gualet.objects.get(id=1).balance
        new_amount_gualet_3 = Gualet.objects.get(id=3).balance

        self.assertEquals(
            old_amount_gualet_1,
            new_amount_gualet_1 + data['amount']
        )
        self.assertEquals(
            old_amount_gualet_3,
            new_amount_gualet_3 - data['amount']
        )

    def test_transaction_create_negative_balance(self):
        old_amount_gualet_1 = Gualet.objects.get(id=1).balance

        data = {
            "address_from": "/api/v1/gualets/1/",
            "address_to": "/api/v1/gualets/3/",
            "amount": old_amount_gualet_1 + 5
        }
        resp = self.api_client.post(
            '/api/v1/transactions/', format="json", data=data
        )

        self.assertHttpBadRequest(resp)
