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


class Procedure(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name.title()

class Visit(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visit_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visit_doctor')
    specialty = models.CharField(max_length=100)
    description = models.TextField()
    medicine = models.ManyToManyField(Medicine)
    procedure = models.ManyToManyField(Procedure)

    def __str__(self):
        return f'On {self.date}, patient - {self.patient} by doctor {self.doctor} '

    class Meta:
        ordering = ['date', ]



