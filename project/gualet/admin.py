from django.contrib import admin
from gualet.models import User
from gualet.models import Gualet
from gualet.models import Transaction

admin.site.register(Gualet)
admin.site.register(Transaction)
