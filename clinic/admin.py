from django.contrib import admin
from .models import Doctor, Procedure, Patient, Medicine, Visit

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Procedure)
admin.site.register(Medicine)
admin.site.register(Visit)
