from django.db import models
from django.contrib.postgres.fields import ArrayField


class MedRecord(models.Model):
    name = models.CharField(max_length=200)
    # Want to be used the allgergy field like this:
    # ([allergy1, reaction1],[allergy2, reaction2])
    allergies = ArrayField(models.CharField(max_length=200, blank=True))
    diagnoses = ArrayField(models.CharField(max_length=200, blank=True))

    def __str__(self):
        return self.name
