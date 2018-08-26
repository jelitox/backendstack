# -*- coding: utf-8 -*-
from django.urls import path, include
from .api.registration import RegistrationAPIView
from .api.login import LoginAPIView
from .api.update import UserRetrieveUpdateAPIView

urlpatterns = [
    path('api/v1/user/', UserRetrieveUpdateAPIView.as_view(), name='api_update_user'),
    path('api/v1/users/', RegistrationAPIView.as_view(), name='api_registration'),
    path('api/v1/users/login/', LoginAPIView.as_view(), name='api_login'),
]