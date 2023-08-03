from django.urls import path, include
from . import views
from rest_framework import routers
from .views import MagangViewSet

router = routers.DefaultRouter()
router.register("magangs", MagangViewSet)


urlpatterns = [
    path("", include(router.urls)),
]