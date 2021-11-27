from .models import Vacancies, Reservation
from rest_framework import serializers

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ['date', 'price']



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['email', 'start_date', 'end_date', 'total_vacancy', 'total_price']