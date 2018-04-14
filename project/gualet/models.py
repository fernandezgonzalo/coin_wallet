import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Gualet(models.Model):
    address = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=100)
    balance = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Address: {}, balance: {}".format(self.address, self.balance)

    def save(self, *args, **kwargs):
        self.address = str(uuid.uuid4())
        super().save(*args, **kwargs)


class Transaction(models.Model):
    address_from = models.ForeignKey(
        Gualet,
        related_name='address_from',
        on_delete=models.CASCADE
    )
    address_to = models.ForeignKey(
        Gualet,
        related_name='address_to',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.address_from.balance - self.amount >= 0:
            self.address_from.balance -= self.amount
            self.address_to.balance += self.amount
            self.address_from.save()
            self.address_to.save()
            super().save(*args, **kwargs)
        else:
            raise ValidationError('amount < 0')

    def __str__(self):
        return "Transaction: from {} --> {} coins --> to {}".format(
            self.address_from,
            self.amount,
            self.address_to
        )
