from django.shortcuts import render
from django.views.generic import FormView
from .forms import EmailCreateFom
from .models import Emailer,EmailContacts
from .helpers import mail_client


class EmailCreateView(FormView):
    model = Emailer
    template_name = "emailer.html"
    form_class=EmailCreateFom
    success_url='/'

    def form_valid(self,form):
        mail=form.cleaned_data["email_list"]
        email_subject=form.cleaned_data["email_subject"]
        attachment=form.cleaned_data["attachment"]
        email_body=form.cleaned_data["email_body"]
        touch=get_object_or_404(EmailContacts,1)

        email_list={i.strip().lower() for i in mail.split(',') }
        reciever_set=[]

        for i in email_list:
            reciever,created=EmailContacts.objects.get_or_create(email=i)
            reciever_set.append(reciever)
            mail_client(i,email_subject,email_body,attachment)
        reciever_set=(*reciever_set,)
        mail=form.save()
        mail.email_reciever.set(reciever_set)   
            
        return super().form_valid(form)
