from django.db import models


# Create your models here.
class BPM(models.Model):
    make_text = models.CharField(max_length = 200)
    model_text = models.CharField(max_length = 200)
    year_number = models.IntegerField(max_length = 4)

    bpm_number = models.IntegerField(max_length = 3)

    last_updated_number = models.DateTimeField('last updated')
