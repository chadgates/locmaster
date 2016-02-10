from rest_framework import serializers
from unlocode.models import Locode


class LocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locode
        fields = ('locode', 'locname', 'locoordinates')
