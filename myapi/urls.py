from django.urls import include, path
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
router.register(r'locations',views.LocationsViewSet, basename="Locations")
router.register(r'landmarks', views.LandmarkViewSet, basename="Landmarks")



urlpatterns = [
    path('', include(router.urls)),
    path('locations/<int:location_id>/landmarks',views.LandmarksbyLocation.as_view(), name="landmarks_by_loaction_id"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]