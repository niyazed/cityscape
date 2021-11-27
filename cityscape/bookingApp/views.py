from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from bookingApp.models import Vacancies, Reservation
from bookingApp.serializers import VacanciesSerializer, ReservationSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.db.models import Q, query
# Create your views here.


def vacany_list(request):
    if request.method == 'GET':
        vac = Vacancies.objects.all()
        ser = VacanciesSerializer(vac, many=True)
        return JsonResponse(ser.data, safe=False)

@csrf_exempt
def reservation(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        vac = Vacancies.objects.filter(Q(date__gte = data['start_date']) & Q(date__lte = data['end_date']))
        if vac.count() == 0:
            return JsonResponse({"error": "No Vacancy avaiable"}, safe=False)

        print(vac)
        ser = VacanciesSerializer(vac, many=True)
        ids = [v.id for v in vac]
        total_price = sum([int(v.price) for v in vac])
        data.update(total_vacancy = vac.count(), total_price = total_price)

        ser = ReservationSerializer(data=data)
        if ser.is_valid():
            ser.save()
            vac.delete()
            # print(ser.data['email'])
            return JsonResponse(ser.data, safe=False)
        return JsonResponse(ser.errors, status=400)