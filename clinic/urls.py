from django.urls import path
from .views import *

urlpatterns = [
    path('patients/', PatientsList.as_view(), name= 'patients_list'),
    path('doctors/', DoctorsList.as_view(), name ='doctors_list'),
    path('procedures/', ProceduresList.as_view(), name = 'procedures_list'),
    path('medicines/', MedicinesList.as_view(), name = 'medicines_list'),
    path('visits/', VisitsList.as_view(), name = 'visits_list'),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name = 'doctor_detail'),
    path('procedure/<int:pk>/', ProcedureDetail.as_view(), name= 'procedure_detail'),
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name= 'medicine_detail'),
    path('visit/<int:pk>/', VisitDetail.as_view(), name = 'visit_detail'),

]