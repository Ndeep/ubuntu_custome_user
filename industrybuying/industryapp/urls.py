from django.conf.urls import url,include
from .views import FileView
from rest_framework.routers import DefaultRouter
from account.views import AccountView

router=DefaultRouter()
router.register(r'files',FileView)

urlpatterns = [
    url(r'account1',AccountView.as_view()),
]