from django.shortcuts import render, get_object_or_404
from .models import Event
from .forms import EventForm,UpdateStatusForm

# Create your views here.

def index(request):
    eventList = Event.objects.all()
    return render(request,'events/index.html',{ 'list' : eventList })

def detail(request, eid):
    temp = eid[:len(eid)-1]
    event = get_object_or_404(Event, id = temp)
    return render(request,'events/detail.html',{ 'event' : event })
    
def createEvent(request):
    if request.user.is_authenticated():
        success = 0
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                e = Event()
                e.eventName = request.POST['eventName']
                e.eventTime = request.POST['eventTime']
                e.eventLocation = request.POST['eventLocation']
                e.eventDescription = request.POST['eventDescription']
                e.eventStatus = request.POST['eventStatus']
                e.save()
                success = 1
        else:
            form = EventForm()
        return render(request,'events/create.html',{ 'form' : form , 'success' : success })
        
def updateStatus(request, eid):
    #if request.user.is_authenticated():
        success = 0
        if request.method == 'POST':
            form = UpdateStatusForm(request.POST)
            if form.is_valid():
                e = Event.objects.get(id = eid)
                e.eventStatus = request.POST.get('eventStatus','idle')
                e.save(update_fields = ['eventStatus'])
                success = 1
        else:
            form = UpdateStatusForm()
        return render(request,'events/updateStatus.html',{ 'form' : form, 'success' : success })
            