# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Show
from .models import ShowVenue
from .serializers import ShowSerializer
from .serializers import ShowVenueSerializer


class ShowList(APIView):
    """
    List all shows, or create a new show.
    """
    def get(self, request, format=None):
        shows = Show.objects.active()
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShowSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowDetail(APIView):
    """
    Retrieve, update or delete a show.
    """

    def _get_object(self, pk):
        try:
            return Show.objects.get(pk=pk)
        except Show.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        show = self._get_object(pk)
        serializer = ShowSerializer(show)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        show = self._get_object(pk)
        serializer = ShowSerializer(show, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        show = self._get_object(pk)
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShowVenueList(APIView):
    """
    List all show venues, or create a new venue.
    """
    def get(self, request, format=None):
        venues = ShowVenue.objects.all()
        serializer = ShowVenueSerializer(venues, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShowVenueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowVenueDetail(APIView):
    """
    Retrieve, update or delete a show venue.
    """

    def _get_object(self, pk):
        try:
            return ShowVenue.objects.get(pk=pk)
        except ShowVenue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        venue = self._get_object(pk)
        serializer = ShowVenueSerializer(venue)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        venue = self._get_object(pk)
        serializer = ShowVenueSerializer(venue, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        venue = self._get_object(pk)
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
