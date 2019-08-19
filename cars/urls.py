from rest_framework import routers

from . import views

app_name = 'cars'
router = routers.SimpleRouter()
router.register(r'listmakes', views.CarMakeViewSet)
urlpatterns = router.urls