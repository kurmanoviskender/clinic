from django.http import request
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Patient, Doctor, Visit, Procedure, Medicine
from .forms import *



def index(request):
    return render(request, 'index.html')



class PatientsListView(ListView):
    model = Patient
    template_name = 'patients_list.html'


class DoctorsListView(ListView):
    model = Doctor
    template_name ='doctors_list.html'


class ProceduresListView(ListView):
    model = Procedure
    template_name = 'procedures_list.html'


class VisitsListView(ListView):
    model = Visit
    template_name = 'visits_list.html'


class MedicinesListView(ListView):
    model = Medicine
    template_name = 'medicines_list.html'


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient_detail.html'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'


class ProcedureDetailView(DetailView):
    model = Procedure
    template_name = 'procedure_detail.html'


class VisitDetailView(DetailView):
    model = Visit
    template_name = 'visit_detail.html'


class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'medicine_detail.html'


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorCreateForm
    template_name = 'doctor_new.html'

    def get_success_url(self):
        return reverse('doctors_list')


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreateForm
    template_name = 'patient_new.html'

    def get_success_url(self):
        return reverse('patients_list')


class ProcedureCreateView(CreateView):
    model = Procedure
    form_class = ProcedureCreateForm
    template_name = 'procedure_new.html'

    def get_success_url(self):
        return reverse('procedures_list')


class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineCreateForm
    template_name = 'medicine_new.html'

    def get_success_url(self):
        return reverse('medicines_list')


class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitCreateForm
    template_name = 'visit_new.html'

    def get_success_url(self):
        return reverse('visits_list')


class PatientEditView(UpdateView):
    model = Patient
    form_class = PatientEditForm
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return reverse('patients_list')


class DoctorEditView(UpdateView):
    model = Doctor
    form_class = DoctorEditForm
    template_name = 'doctor_edit.html'

    def get_success_url(self):
        return reverse('doctors_list')


class ProcedureEditView(UpdateView):
    model = Procedure
    form_class = ProcedureEditForm
    template_name = 'procedure_edit.html'

    def get_success_url(self):
        return reverse('procedures_list')


class MedicineEditView(UpdateView):
    model = Medicine
    form_class = MedicineEditForm
    template_name = 'medicine_edit.html'

    def get_success_url(self):
        return reverse('medicines_list')


class VisitEditView(UpdateView):
    model = Visit
    form_class = VisitEditForm
    template_name = 'visit_edit.html'

    def get_success_url(self):
        return reverse('visits_list')
