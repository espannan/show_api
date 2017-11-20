# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIClient

from .models import Show
from .models import ShowVenue


class ShowTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.venue = ShowVenue.objects.create(
            url='http://www.testvenue.com',
            name='Test Venue',
            address='123 Main St.  San Francisco, CA 94103',
        )

    def test_create_show(self):

        # send the request to create a show
        data = {
            'headliner': 'Test Headliner',
            'openers': 'Test Openers',
            'showtime': '2017-11-21 03:00:00+00:00',
            'show_venue': self.venue.pk,
        }
        request = self.client.post('/shows/', data)

        # verify the request went through
        self.assertEqual(status.HTTP_201_CREATED, request.status_code)

        # verify the show was created
        content = json.loads(request.content)
        show = Show.objects.get(pk=content['id'])
        self.assertEqual('Test Headliner', show.headliner)
        self.assertEqual('Test Openers', show.openers)
        self.assertEqual('2017-11-21 03:00:00+00:00', str(show.showtime))
        self.assertEqual(self.venue, show.show_venue)

    def test_get_show(self):

        # make sure a show is in the database
        self.test_create_show()

        # send the request to get a show
        request = self.client.get('/shows/1')

        # verify the request went through
        self.assertEqual(status.HTTP_200_OK, request.status_code)

        # verify the show info is correct
        content = json.loads(request.content)
        show = Show.objects.get(pk=content['id'])
        self.assertEqual('Test Headliner', show.headliner)
        self.assertEqual('Test Openers', show.openers)
        self.assertEqual('2017-11-21 03:00:00+00:00', str(show.showtime))
        self.assertEqual(self.venue, show.show_venue)

    def test_update_show(self):

        # make sure a show is in the database
        self.test_create_show()

        # send the request to update a show
        data = {
            'openers': 'New Openers',
        }
        request = self.client.put('/shows/1', data)

        # verify the request went through
        self.assertEqual(status.HTTP_200_OK, request.status_code)

        # verify the show info is correct
        show = Show.objects.get(pk=1)
        self.assertEqual('Test Headliner', show.headliner)
        self.assertEqual('New Openers', show.openers)
        self.assertEqual('2017-11-21 03:00:00+00:00', str(show.showtime))
        self.assertEqual(self.venue, show.show_venue)

    def test_delete_show(self):

        # make sure a show is in the database
        self.test_create_show()

        self.assertEqual(Show.objects.count(), 1)
        self.assertEqual(Show.objects.active().count(), 1)

        # send the request to delete a show
        request = self.client.delete('/shows/1')

        # verify the request went through
        self.assertEqual(status.HTTP_204_NO_CONTENT, request.status_code)

        # verify the show is inactive
        self.assertEqual(Show.objects.active().count(), 0)
        self.assertEqual(Show.objects.count(), 1)


class ShowVenueTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_venue(self):

        # send the request to create a venue
        data = {
            'url': 'http://www.testvenue.com',
            'name': 'Test Venue',
            'address': '123 Main St.  San Francisco, CA 94103',
        }
        request = self.client.post('/show-venues/', data)

        # verify the request went through
        self.assertEqual(status.HTTP_201_CREATED, request.status_code)

        # verify the venue was created
        content = json.loads(request.content)
        venue = ShowVenue.objects.get(pk=content['id'])
        self.assertEqual('http://www.testvenue.com', venue.url)
        self.assertEqual('Test Venue', venue.name)
        self.assertEqual('123 Main St.  San Francisco, CA 94103', venue.address)

    def test_get_venue(self):

        # make sure a venue is in the database
        self.test_create_venue()

        # send the request to get a venue
        request = self.client.get('/show-venues/1')

        # verify the request went through
        self.assertEqual(status.HTTP_200_OK, request.status_code)

        # verify the venue info is correct
        content = json.loads(request.content)
        venue = ShowVenue.objects.get(pk=content['id'])
        self.assertEqual('http://www.testvenue.com', venue.url)
        self.assertEqual('Test Venue', venue.name)
        self.assertEqual('123 Main St.  San Francisco, CA 94103', venue.address)

    def test_update_venue(self):

        # make sure a venue is in the database
        self.test_create_venue()

        # send the request to update a venue
        data = {
            'name': 'New Name',
        }
        request = self.client.put('/show-venues/1', data)

        # verify the request went through
        self.assertEqual(status.HTTP_200_OK, request.status_code)

        # verify the venue info is correct
        venue = ShowVenue.objects.get(pk=1)
        self.assertEqual('http://www.testvenue.com', venue.url)
        self.assertEqual('New Name', venue.name)
        self.assertEqual('123 Main St.  San Francisco, CA 94103', venue.address)

    def test_delete_venue(self):

        # make sure a venue is in the database
        self.test_create_venue()

        self.assertEqual(ShowVenue.objects.count(), 1)

        # send the request to delete a venue
        request = self.client.delete('/show-venues/1')

        # verify the request went through
        self.assertEqual(status.HTTP_204_NO_CONTENT, request.status_code)

        # verify the venue is gone
        self.assertEqual(ShowVenue.objects.count(), 0)
