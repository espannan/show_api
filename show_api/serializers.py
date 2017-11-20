from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Show
from .models import ShowVenue


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        exclude = ('removed_at',)
        validators = [
            UniqueTogetherValidator(
                queryset=Show.objects.active(),
                fields=('headliner', 'showtime', 'show_venue')
            )
        ]

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ShowSerializer, self).__init__(*args, **kwargs)


class ShowVenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowVenue
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ShowVenueSerializer, self).__init__(*args, **kwargs)
