
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.views import ContactViewSet,UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('contact', ContactViewSet)
router.register('user', UserViewSet,basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-login/', obtain_auth_token),

]
