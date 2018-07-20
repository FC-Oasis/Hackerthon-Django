from django.shortcuts import render



from csv import writer
from io import StringIO

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from .models import Observation


def index(request):
    """Show index page."""
    template = get_template("index.html")
    variables = Context({
        "head_title": "Open Weather Station",
        "page_title": "Open Weather Station",
        "page_body": "Open Weather Station is the reference project for Full "
                     "Stack Embedded 2016. We hope you like it!",
    })
    output = template.render(variables)
    return HttpResponse(output)


def csv_stations(request):
    """Return CSV of available stations."""
    response = StringIO()
    response.write("name,id,longitude,latitude,elevation,activated,deactivated,"
                   "description\r\n")
    csv_renderer = writer(response)
    csv_renderer.writerows(
        ((station.name, station.station_id, station.longitude,
          station.latitude, station.elevation, station.activated,
          station.deactivated, station.description))
        for station in Station.objects.all()
    )
    response.seek(0)
    return HttpResponse(response)


def csv_observation_request(request, station, start, end):
    """Return CSV of observations in requested time range."""
    response = StringIO()
    response.write("date,station_id,temperature,relative_humidity,"
                   "precipitation,wind_speed,wind_direction,pressure\r\n")
    csv_renderer = writer(response)
    csv_renderer.writerows(
        ((obs.obs_date, obs.station.station_id, obs.temperature,
          obs.relative_humidity,
          obs.precipitation, obs.wind_speed, obs.wind_direction, obs.pressure))
        for obs
        in Observation.objects.filter(
            station__station_id=station,
            obs_date__gte=start,
            obs_date__lte=end
        )
    )
    response.seek(0)
    return HttpResponse(response)
