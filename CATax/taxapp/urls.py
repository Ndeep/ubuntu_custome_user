from django.urls import path,include
from rest_framework import routers
from taxapp.views import TaxViewSet,TaxDetailViewset


router=routers.DefaultRouter()
router.register(r'taxdetail',TaxDetailViewset)
router.register(r'tax',TaxViewSet)


urlpatterns = router.urls