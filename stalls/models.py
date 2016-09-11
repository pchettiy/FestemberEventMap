from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Stall(models.Model):   
    stallId = models.IntegerField(primary_key = True)
    #slug = models.SlugField(max_length = 20 , unique = True, default = '0')
    stallName = models.CharField(max_length=100, default = 'Not Available')
    stallDescription = models.CharField(max_length=250, default = 'Not Available')
    stallLocation = models.CharField(max_length=100, default = 'Not Available')
    
    class Meta:
        ordering = ('stallId',)
        
        
    def __unicode__(self):
        return self.stallName
        
    def get_absolute_url(self):
        return reverse('stalls:detail' , kwargs = { "slug" : str(self.stallId) })
        
    	 
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""