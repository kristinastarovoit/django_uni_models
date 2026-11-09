from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Studentenausweis(models.Model):
    ausweis_nummer = models.CharField(max_length=80, unique=True)


class Semester(models.Model):
    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Wochentag(models.TextChoices):
    MONTAG = "Montag"
    DIENSTAG = "Dienstag"
    MITTWOCH = "Mittwoch"
    DONNERSTAG = "Donnerstag"
    FREITAG = "Freitag"


class Kurs(models.Model):
    name = models.CharField(max_length=60)
    raum = models.CharField(max_length=40, default="Aula 1")
    uhrzeit = models.TimeField()
    wochentag = models.CharField(max_length=10, choices=Wochentag.choices)

    def __str__(self):
        return f"{self.name}"


class Kursbeschreibung(models.Model):
    beschreibung = models.CharField(max_length=400)


class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
