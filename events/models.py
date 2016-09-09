from django.db import models

# Create your models here.

class Event(models.Model):
	event_name= models.CharField(max_length=100)
	#event_pics= location of pics in server
	event_time = models.DateTimeField()
	event_location = models.CharField(max_length=100)
	STATUS_CHOICES = (
		(ONGOING,"ongoing"),
		(COMPLETED,"completed"),
		(GOING_TO_START,"going_to_start"),
		(IDLE,"idle"),
		)
	event_status = models.CharField(
		max_length=100,
		choices=STATUS_CHOICES,
		default=IDLE,
		)
	event_description = models.CharField(max_length=200)
