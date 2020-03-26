from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientsListView.as_view(), name= 'patients_list'),
    path('patients/', PatientsListView.as_view(), name= 'patients_list'),
    path('doctors/', DoctorsListView.as_view(), name ='doctors_list'),
    path('procedures/', ProceduresListView.as_view(), name = 'procedures_list'),
    path('medicines/', MedicinesListView.as_view(), name = 'medicines_list'),
    path('visits/', VisitsListView.as_view(), name = 'visits_list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name = 'doctor_detail'),
    path('procedure/<int:pk>/', ProcedureDetailView.as_view(), name= 'procedure_detail'),
    path('medicine/<int:pk>/', MedicineDetailView.as_view(), name= 'medicine_detail'),
    path('visit/<int:pk>/', VisitDetailView.as_view(), name = 'visit_detail'),
    path('doctors/new/', DoctorCreateView.as_view(), name ='new_doctor'),
    path('patients/new/', PatientCreateView.as_view(), name = 'new_patient'),
    path('procedures/new/', ProcedureCreateView.as_view(), name = 'new_procedure'),
    path('medicines/new/', MedicineCreateView.as_view(), name ='new_medicine'),
    path('visits/new/', VisitCreateView.as_view(), name='new_visit'),
    path('patient/<int:pk>/edit/', PatientEditView.as_view(), name ='patient_edit'),
    path('doctor/<int:pk>/edit/', DoctorEditView.as_view(), name ='doctor_edit'),
    path('procedure/<int:pk>/edit/', ProcedureEditView.as_view(), name ='procedure_edit'),
    path('medicine/<int:pk>/edit/', MedicineEditView.as_view(), name='medicine_edit'),
    path('visit/<int:pk>/edit/', VisitEditView.as_view(), name='visit_edit'),
    path('patient/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name = 'doctor_delete'),
    path('procedure/<int:pk>/delete/', ProcedureDeleteView.as_view(), name='procedure_delete'),
    path('medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name = 'medicine_delete'),
    path('visit/<int:pk>/delete/', VisitDeleteView.as_view(), name='visit_delete'),

]