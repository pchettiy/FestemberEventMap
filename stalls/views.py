from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Stall
from .forms import StallForm
# Create your views here.

def createStall(request):
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


def index(request):
	stallList = Stall.objects.all()
	return render(request, 'stalls/index.html', { 'list' : stallList })

def detail(request, sid):
        temp = sid[:len(sid)-1]
        stall = get_object_or_404(Stall, stallId = temp)
        return render(request, 'stalls/detail.html',{ 'stall' : stall })
