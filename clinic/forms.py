from django import forms
from .models import *


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class ProcedureCreateForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


class VisitCreateForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['specialty']

    def save(self):
        visit = super().save(commit=False)
        visit.specialty = visit.doctor.specialty
        visit.save()
        self.save_m2m()
        return visit


class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class ProcedureEditForm(forms.ModelForm):
    class Meta:
        model = Procedure
        fields = '__all__'


class MedicineEditForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


class VisitEditForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['specialty']

    def save(self):
        visit = super().save(commit=False)
        visit.specialty = visit.doctor.specialty
        visit.save()
        self.save_m2m()
        return visit




