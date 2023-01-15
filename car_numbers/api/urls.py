from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, plate_add, plate_get, plates_generate

app_name = 'api'

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('plate/get/<uuid:id>/', plate_get),
    path('plate/add/', plate_add),
    path('plate/generate/<int:amount>/', plates_generate),
    path('plate/generate/', plates_generate),
    path('', include(router.urls)),
]