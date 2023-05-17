from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class EmailContacts(models.Model):
    email=models.EmailField(_("email address"), max_length=254)

class Emailer(models.Model):
    email_reciever=models.ManyToManyField(EmailContacts, verbose_name=_("email recipient"))
    date_sent = models.DateTimeField(_("email date"), auto_now_add=True)
    email_subject = models.CharField(_("email subject"), max_length=250)
    attachment = models.FileField(_("email attachemt"), upload_to='attachments')
    email_body=models.TextField(_("email message"))