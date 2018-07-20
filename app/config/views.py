import datetime

from django.http import HttpResponse
from django.shortcuts import render

from observation.models import Record

#
# def index(request):
#     return render(request, 'main.html')


def index(request):
    Record.objects.create(
        humidity=40,
        temperature=29,
        recorded_at=datetime.datetime.strptime('2018-07-20T16:00:36', '%Y-%m-%dT%H:%M:%S'),
    )

    data = Record.objects.first()
    context = {
        'data': data,
    }
    return render(request, 'main.html', context)
