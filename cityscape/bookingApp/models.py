from django.db import models

# Create your models here.
class Vacancies(models.Model):
    date = models.CharField(max_length=150)
    price = models.CharField(max_length=150)

class Reservation(models.Model):
    email = models.CharField(max_length=150)
    start_date = models.CharField(max_length=150)
    end_date = models.CharField(max_length=150)
    total_vacancy = models.CharField(max_length=150)
    total_price = models.CharField(max_length=150)