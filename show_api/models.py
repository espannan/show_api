# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class ShowVenue(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return '{} ({})'.format(self.name, self.url)


class ShowQueryset(models.QuerySet):
    def active(self):
        return self.filter(removed_at__isnull=True)


class Show(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(null=True)

    objects = ShowQueryset.as_manager()

    headliner = models.CharField(max_length=255)
    openers = models.CharField(max_length=255, null=True, blank=True)
    showtime = models.DateTimeField()

    show_venue = models.ForeignKey('ShowVenue')

    class Meta:
        unique_together = (
            ('show_venue', 'headliner', 'showtime'),
        )

    def delete(self):
        """
        Set a show as inactive rather than deleting from the database
        """
        self.removed_at = timezone.now()
        self.save()

    def _delete(self):
        """
        Actually delete a Show instance

        Intended for internal use.
        """
        super(models.Model, self).delete()

    def __str__(self):
        return '{} ({})'.format(self.headliner, self.show_venue.name)
