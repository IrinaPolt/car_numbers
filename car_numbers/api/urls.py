from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, plate_add, plates_list #, plates_generate

app_name = 'api'

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('plate/get/', plates_list),
    path('plate/add/', plate_add),
    # path('plate/generate/', plates_generate),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]