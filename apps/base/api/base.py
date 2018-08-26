# -*- coding: utf-8 -*-
from apps.base.models import Countries, Cities, AcademicLevel
from apps.base.serializers import  CountriesSerializer, CitiesSerializer, AcademicLevelSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


""" Countries Rest API View """


class CountriesList(generics.ListCreateAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer


""" Cities Rest API View """


class CitiesList(generics.ListCreateAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


""" Academic Level Rest API View """


class AcademicLevelList(generics.ListCreateAPIView):
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer


""" User Profile Rest API View """


class UserProfileApiView(APIView):

    def get(self, request):
        """
        Cities GET Request

        :param request:
        :return: response
        """
        try:
            user_id = 2
            program_id = 3
            enabled = True
            # snippets = Snippet.objects.all()
            # serializer = SnippetSerializer(snippets, many=True)
            # return JsonResponse(serializer.data, safe=False)
            dashboard_list = Dashboard.objects.filter(enabled=enabled, program_id=program_id,
                                                      user_id=user_id).all().values(
                'dashboard_id', 'duid', 'user_id', 'program_id', 'name',
                'description', 'params', 'enabled', 'shared',
                'published', 'allow_filtering', 'slug')
            data = JSONRenderer().render(dashboard_list)
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            print('Dashboard API Error: %s ' % e)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
        Dashboard POST Request

        :param request:
        :return: response
        """
        try:
            data = request.data
            if data:
                serializer = DashboardSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status.HTTP_201_CREATED)
            return Response(status.HTTP_400_BAD_REQUEST)
        except NameError:
            return Response(status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Dashboard PUT Request

        :param request:
        :return: response
        """
        try:

            return Response(status.HTTP_400_BAD_REQUEST)
        except NameError:
            return Response(status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Dashboard DELETE Request

        :param request:
        :return: response
        """
        try:

            return Response(status.HTTP_400_BAD_REQUEST)
        except NameError:
            return Response(status.HTTP_400_BAD_REQUEST)
