
from django.contrib import admin
from django.conf.urls import *
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token 
from api import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'machines', views.MachineViewSet)
router.register(r'customers', views.CustomerViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
