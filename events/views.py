from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Event
import json
# Create your views here.

def allEvents(request):
	eventList=Event.objects.all()
	
	results=[ob.as_json() for ob in eventList]
	return HttpResponse(json.dumps(results),content_type='application/json')


