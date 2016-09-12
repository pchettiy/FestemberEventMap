from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import Stall
from .forms import StallForm
# Create your views here.

def index(request):
	stallList = Stall.objects.all()
	data= serializers.serialize('json',stallList )
	#return render(request, 'stalls/index.html', { 'list' : stallList })
	return HttpResponse(data,content_type="application/json")

def detail(request, sid):
        temp = sid[:len(sid)-1]
        stall = get_object_or_404(Stall, stallId = temp)
        return render(request, 'stalls/detail.html',{ 'stall' : stall })
"""
def create(request):
	if request.method=='POST':
		s=Stall()
		s.stallId=request.POST['stallId']
		s.stallName=request.POST['stallName']
		s.stallDescription = request.POST['stallDescription']
		s.stallLocation = request.POST['stallLocation']
		s.save()

	return render(request,'stalls/entry_created.html')

"""
"""
def createStall(request):
	#How do you authenticate?Where is this taking place?
    if request.user.is_authenticated():
        success = 0
        if request.method == 'POST':
            form = StallForm(request.POST)
            if form.is_valid():
                s = Stall()
                s.stallId = request.POST['stallId']
                s.stallName = request.POST['stallName']
                s.stallDescription = request.POST['stallDescription']
                s.stallLocation = request.POST['stallLocation']
                s.save()
                success = 1
        else:
            form = StallForm()
        return render(request,'stalls/create.html', { 'form' : form, 'success' : success})    

"""
