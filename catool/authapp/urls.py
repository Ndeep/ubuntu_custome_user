from django.urls import path
from authapp.views import RegisterView


urlpatterns=[
    path('register/',RegisterView.as_view())
]