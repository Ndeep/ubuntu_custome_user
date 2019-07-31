from django.urls import path,include
from youtubeapp.views import view_books

urlpatterns=[
    path(r'', view_books),
]