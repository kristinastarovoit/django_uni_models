from django.db import models


class Wochentag(models.TextChoices):
    """
    class for Kurs, sets choices for the weekday
    """
    MONTAG = "Montag"
    DIENSTAG = "Dienstag"
    MITTWOCH = "Mittwoch"
    DONNERSTAG = "Donnerstag"
    FREITAG = "Freitag"

class Student(models.Model):
    """
    one-to-one Studentenausweis
    many-to-many Kurs
    """
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()
    kurse = models.ManyToManyField("Kurs")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Studentenausweis(models.Model):
    """
    one-to-one Student
    deleting the student deletes the related Studentenausweis
    """
    ausweis_nummer = models.CharField(max_length=80, unique=True)
    student = models.OneToOneField("Student", on_delete=models.CASCADE)


class Semester(models.Model):
    """
    one-to-many Kurs
    deleting the Semester or Kurs doesn't affect the other Class
    """
    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name}"


class Kurs(models.Model):  
    """
    many-to-one Semester
    the semester can't be deleted as long as there are Kurse related
    many-to-one Professor
    deleting the professor doesn't affect the Kurs
    one-to-one Kursbeschreibung
    deleting the Kurs deletes Kursbeschreibung
    many-to-many Student
    """
    name = models.CharField(max_length=60)
    raum = models.CharField(max_length=40, default="Aula 1")
    uhrzeit = models.TimeField()
    wochentag = models.CharField(max_length=10, choices=Wochentag.choices)
    semester = models.ForeignKey("Semester", on_delete=models.PROTECT)
    professor = models.ForeignKey("Professor", on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.name}"


class Kursbeschreibung(models.Model):
    """
    one-to-one Kurs
    deleting the Kurs deletes Kursbeschreibung
    """
    beschreibung = models.CharField(max_length=400)
    kurs = models.OneToOneField("Kurs", on_delete=models.CASCADE)


class Professor(models.Model):
    """
    one-to-many Kurs
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
