import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Record


def add(request):
    if request.method == 'POST':
        record = Record.objects.create(
            humidity=int(request.POST.get('Humidity')),
            temperature=int(request.POST.get('Temperature')),
            recorded_at=datetime.datetime.strptime(request.POST.get('time'), '%Y-%m-%dT%H:%M:%S'),
        )
        print(record)
        return HttpResponse('OK', status=200)
    else:
        return render(request, 'observation/add.html')
