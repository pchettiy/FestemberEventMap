from django.db import models

# Create your models here.

class Event(models.Model):
	event_name= models.CharField(max_length=100)
	#event_pics= location of pics in server
	event_time = models.DateTimeField()
	event_location = models.CharField(max_length=100)
	"""
	STATUS_CHOICES = (
		(ONGOING,"ongoing"),
		(COMPLETED,"completed"),
		(GOING_TO_START,"going_to_start"),
		(IDLE,"idle"),
		)
	"""
	event_status = models.CharField(
		max_length=100
		#choices=STATUS_CHOICES,
		#default=IDLE,
		)
	event_description = models.CharField(max_length=200)

	def as_json(self):
		return dict(id=self.id,
			event_name=self.event_name,
			event_time=self.event_time,
			event_location=self.event_location,
			event_description=self.event_description,
			event_status=self.event_status)
