import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .models import Record


def add(request):
    if request.method == 'post':
        record = Record.objects.create(
            humidity=int(request.POST.get('Humidity')),
            temperature=int(request.POST.get('Temperature')),
            recorded_at=datetime.strptime(request.POST.get('time')),
        )
        return HttpResponse('OK', status=200)
    else:
        return render(request, 'observation/add.html')
