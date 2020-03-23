from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, UpdateView
from .models import Patient, Doctor, Visit, Procedure, Medicine


class PatientsList(ListView):
    model = Patient
    template_name = 'patients_list.html'


class DoctorsList(ListView):
    model = Doctor
    template_name ='doctors_list.html'


class ProceduresList(ListView):
    model = Procedure
    template_name = 'procedures_list.html'


class VisitsList(ListView):
    model = Visit
    template_name = 'visits_list.html'


class MedicinesList(ListView):
    model = Medicine
    template_name = 'medicines_list.html'


class PatientDetail(DetailView):
    model = Patient
    template_name = 'patient_detail.html'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'


class ProcedureDetail(DetailView):
    model = Procedure
    template_name = 'procedure_detail.html'


class VisitDetail(DetailView):
    model = Visit
    template_name = 'visit_detail.html'


class MedicineDetail(DetailView):
    model = Medicine
    template_name = 'medicine_detail.html'
