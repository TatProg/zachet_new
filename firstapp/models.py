from django.conf import settings
from django.db import models


class Sotrudnik(models.Model):
    name_f = models.CharField(max_length=200)
    name_i = models.CharField(max_length=200)
    name_o = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # birth_date = models.CharField(max_length=200)
    birth_date = models.DateField
    education = models.CharField(max_length=200)
    attestat_form = models.CharField(max_length=200)

    def __str__(self):
        return self.title
# Create your models here.
