from .models import Emailer,EmailContacts
from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _


class EmailCreateFom(ModelForm):
    
    email_list=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Enter ther list of subscribers here (seperated by ",")'}))

    class Meta:
        model=Emailer
        fields=[
            'email_subject',
            'attachment',
            'email_body',
        ]
        widgets={     
            'email_subject':forms.TextInput(attrs={'class': "form-control"}),
            'email_body':forms.Textarea(attrs={'class': "form-control"}),
                    
          
          
        }