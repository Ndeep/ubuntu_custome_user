from django.contrib import admin
from django.urls import path
from account.views import AccountView,ClientView,ClientDetail

urlpatterns = [
    path('account/', AccountView.as_view()),
    path('client/',ClientView.as_view()),
    path('client/<int:pk>',ClientDetail.as_view())
]
