from django.db import models


class year(models.Model):
    #2014-2015
    year = models.TextField()


class course(models.Model):
    #2.DBH LOE,2DBH,2...
    name_es = models.TextField()
    name_eu = models.TextField()
    abv_es = models.TextField()
    abv_eu = models.TextField()
    order = models.IntegerField()


class period(models.Model):
    name_es = models.TextField()
    name_eu = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.name_eu


class subject(models.Model):
    name_es = models.TextField()
    name_eu = models.TextField()
    abv_es = models.TextField()
    abv_eu = models.TextField()
    course = models.ForeignKey(course)

    def __str__(self):
        return self.name_eu + "/" + self.name_es


class student(models.Model):
    uniquename = models.TextField(primary_key=True)
    educacode = models.TextField()
    fullname = models.TextField()
    birthdate = models.DateField()
    primaryschool = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
class grade(models.Model):
    year = models.ForeignKey(year)
    subject = models.ForeignKey(subject)
    period = models.ForeignKey(period)
    student = models.ForeignKey(student)
    grade = models.IntegerField()

    def __str__(self):
        return self.student.name + "," + self.subject.abv_es + ":" + self.grade


class yeardata(models.Model):
    #2015,Asier,D,3.DBH,3A
    LANGUAGES_CHOICES = (
    ('A', 'A'),
    ('G', 'G'),
    ('D', 'D'),
    )

    PROMOTION_CHOICES = (
    ('ORD', 'Ordinary Ev.'),
    ('EXT', 'Extraordinary Ev.'),
    ('AUTO', 'Automatically, can\'t repeat'),
    ('NO', 'Notpromoting'),
    )

    year = models.ForeignKey(year)
    student = models.ForeignKey(student)
    languague = models.TextField(choices=LANGUAGES_CHOICES)
    course = models.ForeignKey(course)
    group = models.TextField()
    repeating = models.BooleanField()
    promoting = models.TextField(choices=PROMOTION_CHOICES,
        null=True, blank=True)

    #when importing from educa's csv, get students course as highest (cause lowers are from pending subjects)

