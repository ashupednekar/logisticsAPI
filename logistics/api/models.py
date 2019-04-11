from django.db import models

# Create your model here.
class Features(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)