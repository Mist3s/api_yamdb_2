from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (APIGetToken, APISignup, UsersViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(
    'users',
    UsersViewSet,
    basename='users'
)

urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
    path('v1/', include(router_v1.urls)),
]
