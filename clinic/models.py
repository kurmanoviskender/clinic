from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    M = 'male'
    F = 'female'
    sex = models.CharField(choices=[(M, 'male'), (F, 'female')], max_length=6)
    address = models.CharField(max_length=120)
    passport = models.CharField(max_length=55)
    insurance = models.CharField(max_length=55)

    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']


class Procedure(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Medicine(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Specialty(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title.title()


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='doctor_specialty')

    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']


class Visit(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visit_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visit_doctor')
    specialty = models.CharField(max_length=100)
    description = models.TextField()
    medicine = models.ManyToManyField(Medicine, related_name='visit_medicine')
    procedure = models.ManyToManyField(Procedure, related_name='visit_procedure')

    def __str__(self):
        return f'On {self.date}, patient - {self.patient} by doctor {self.doctor} '

    class Meta:
        ordering = ['-date', ]
