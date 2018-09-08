from django.db import models

# Create your models here.

class websites(models.Model):
    website = models.TextField(blank=True, null=True)