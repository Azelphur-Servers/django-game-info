from django.conf.urls import url, include
from rest_framework import routers
from .views import ServerViewSet

router = routers.DefaultRouter()
router.register(r'server', ServerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls), name='game_info'),
]
