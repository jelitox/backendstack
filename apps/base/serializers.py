# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Countries, Cities, AcademicLevel


""" Country Serializers."""


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ('name',
                  'country_code')


""" City Serializers."""


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = (
            'name',
            'country')




""" Academic Level Serializers."""


class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = (
            'name',
            'description',
            'enabled')
