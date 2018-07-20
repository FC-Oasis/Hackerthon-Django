import datetime

from django.http import HttpResponse
from django.shortcuts import render

from observation.models import Record


def index(request):
    data = Record.objects.first()
    context = {
        'data': data,
    }
    return render(request, 'main.html', context)
