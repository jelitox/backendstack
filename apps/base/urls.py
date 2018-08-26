# -*- coding: utf-8 -*-
from django.urls import include, path
from .api.base import CountriesList, CitiesList, AcademicLevelList, UserProfileApiView

urlpatterns = [
    #### API V1 ###
    # API v1 Countries
    path('api/v1/services/countries/',CountriesList.as_view(), name='api_countries'),
    # API v1 Cities
    path('api/v1/services/cities/', CitiesList.as_view(), name='api_cities'),
    # API v1 Cities
    path('api/v1/services/academiclevel/', AcademicLevelList.as_view(), name = 'api_academic_level')
]
