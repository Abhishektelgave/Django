from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime , timedelta

# Create your views here.
def datetime_with_offset(request):
    now = datetime.now()
    offset=4
    four_hours_after = now + timedelta(hours=offset)
    four_hours_before = now - timedelta(hours=offset)
    html=f"<html><body><h1>Current Date and Time:</h1><p>{ now }</p><p>four hours after:{ four_hours_after }</p><p>four hours after:{ four_hours_before }</p></body></html>"
    return HttpResponse(html)