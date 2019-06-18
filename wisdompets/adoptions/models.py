from django.db import models

class Pet(models.Model):
  SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

  name = models.CharField(max_length=100)
  submitter = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  breed = models.CharField(max_length=100, blank=True)
  description = models.TextField()


class Vaccine(models.Model):
  name = models.CharField(max_length=50)
