from django.contrib import admin
from .models import Emailer, EmailContacts
# Register your models here.
admin.site.register(Emailer)
admin.site.register(EmailContacts)