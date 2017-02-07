from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

UPLOADS_DIR = getattr(settings, "UPLOADS_DIR", "uploads")

# Create your models here.
class Professional(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200, default='')
    profile = models.CharField(max_length=200)
    team = models.ForeignKey('mParkCore.Team', related_name='professionals')

    def __str__(self):
        return self.name + ' ' + self.last_name + '(' + self.profile + ')'

class Team(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class CareLinks(models.Model):
    professional = models.ForeignKey('mParkCore.Professional', related_name='professionals')
    patient = models.ForeignKey('mParkCore.Patient', related_name='patients')
    created_date = models.DateTimeField(default=timezone.now)
    approved_link = models.BooleanField(default=False)

    def approve(self):
        self.approved_link = True
        self.save()

    def cancel(self):
        self.approved_link = False
        self.save()

    def __str__(self):
        return self.professional + ' - ' + self.patient

class Patient(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email= models.CharField(max_length=200, default='')
    profile = models.CharField(max_length=200, default='Parkinson')
    code = models.CharField(max_length=200, unique=True)

    def getAll(self):
        return self.name

    def searchByUser(self, myUser):
        return self.patients.filter(user=myUser)

    def searchByCode(self, myCode):
        return self.patients.filter(code=myCode)

    def __str__(self):
        return self.name + ' ' + self.last_name + '(' + self.profile + ')'

class Session(models.Model):
    patient = models.ForeignKey('mParkCore.Patient', related_name='sessions')
    professional = models.ForeignKey('mParkCore.Professional', related_name='sessions')
    phase_I_duration = models.CharField(max_length=200)
    phase_II_duration = models.CharField(max_length=200)
    phase_III_duration = models.CharField(max_length=200)
    phase_IV_duration = models.CharField(max_length=200)
    phase_V_duration = models.CharField(max_length=200)
    min_BPM = models.CharField(max_length=200, default='80')
    max_BPM = models.CharField(max_length=200, default='140')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name + ' ' + self.professional.name

class SessionFile(models.Model):
    patient = models.ForeignKey('mParkCore.Patient', related_name='session_files')
    file = models.FileField(upload_to=UPLOADS_DIR)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('mParkCore.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)