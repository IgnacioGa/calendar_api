from django.urls import path

from events.views import EventViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', EventViewSet, basename='events')

urlpatterns = router.urls