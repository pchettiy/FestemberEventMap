from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Event(models.Model):
    STATUS_CHOICES = [    ('ONGOING' , "Ongoing"),
                          ('COMPLETED' , "Completed"),
                	    ('GOING_TO_START' , "Going to start"),
                		('IDLE' , "Idle"),
                	]    
    
    
    eventName = models.CharField(max_length=100, blank = False)
	#event_pics= location of pics in server
    eventTime = models.DateTimeField(blank = False)
    eventLocation = models.CharField(max_length=100, default = 'Not Available')
    eventStatus = models.CharField(max_length = 100, choices = STATUS_CHOICES, default = 'IDLE')
    eventDescription = models.CharField(max_length=200, default = 'Not Available')
    
    class Meta:
        ordering = ('eventTime',)
        
    def __unicode__(self):
        return self.eventName
        
    def get_absolute_url(self):
        return reverse("events:detail", kwargs = { "slug" : self.id })
        
