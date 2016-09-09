from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Stall
# Create your views here.

"""
def index(request):
	return HttpResponse("You are at stalls index")
"""

def index(request):
	all_stalls_list= Stall.objects.all()
	template=loader.get_template('stalls/index.html')
	context={
		'latest_stalls_list': all_stalls_list,
	}
	#output = ', '.join([s.stall_name for s in all_stalls_list])
	return render(request, 'stalls/index.html',context)

def detail(request, stall_id):
	stall= get_object_or_404(Stall, pk=stall_id)
	return render(request, 'stalls/detail.html',{'stall':stall})
