from .views import EmailCreateView
from django.urls import path
app_name ='emailer'

urlpatterns = [
  path('', EmailCreateView.as_view(),name='emailer')
]