from django import forms
from .models import Stall

class StallForm(forms.Form):
    stallId = forms.IntegerField(label='Stall ID',widget=forms.NumberInput(attrs={'placeholder':'Stall ID'}))
    stallName = forms.CharField(max_length=100,label='Stall Name',widget=forms.TextInput(attrs={'placeholder': 'stall name'})) 
    stallDescription = forms.CharField(max_length=250,label='Description',widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    stallLocation = forms.CharField(max_length=100,label='Location',widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    
    class Meta:
        model = Stall
        fields = ('stallId','stallName','stallDescription','stallLocation',)

    def clean_stallId(self):
        cd = self.cleaned_data
        if Stall.objects.filter(stallId = cd['stallId']).count():
            raise forms.ValidationError('\nThe given Stall Id already exists\n')
        return cd['stallId']
        
    def clean_stallName(self):
        cd = self.cleaned_data
        if cd['stallName'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        return cd['stallName']
    
    def clean_stallLocation(self):
        cd = self.cleaned_data
        if cd['stallLocation'] is None:
            raise forms.ValidationError('\nThis field is required.\n')
        return cd['stallLocation']
        
        
        