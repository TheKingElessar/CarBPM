from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class CarBPM(models.Model):
    car_make_text = models.CharField("Car Make", max_length = 200)
    car_model_text = models.CharField("Car Model", max_length = 200)
    car_year_number = models.PositiveIntegerField("Car Year", validators = [MaxValueValidator(9999)])

    car_bpm_number = models.PositiveIntegerField("Car BPM", validators = [MaxValueValidator(999)])

    car_last_updated_date = models.DateTimeField("Last Modified")

    def __str__(self):
        return f"{self.car_make_text} {self.car_model_text} ({self.car_year_number}) - {self.car_bpm_number}"
