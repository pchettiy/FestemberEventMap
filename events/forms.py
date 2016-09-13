from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    eventName = forms.CharField(max_length = 100,label='Event Name',widget = forms.TextInput(attrs={'placeholder': 'event name'}))
    eventTime = forms.DateTimeField(label='Event Date and Time',widget = forms.DateTimeInput())
    
    def clean_eventName(self):
        cd = self.cleaned_data
        if cd['eventName'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        return cd['eventName']
        
    def clean_eventTime(self):
        cd = self.cleaned_data
        if cd['eventTime'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        return cd['eventTime']
    
    class Meta:
        model = Event
        fields = ('eventName','eventTime','eventLocation','eventStatus','eventDescription',)
        
class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('eventStatus',)