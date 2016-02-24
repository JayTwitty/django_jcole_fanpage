from django.db import models
import datetime

# Create your models here.
from django.forms import TimeInput


class Jcole(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    event_time = models.TimeField()
    event_location = models.CharField(max_length=50)
    ticket_info = models.CharField(max_length=100)

    def __str__(self):
        return"{} {} {}".format(self.event_name, self.event_date, self.event_location)

