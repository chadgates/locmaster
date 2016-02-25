from rest_framework import serializers
from unlocode.models import Locode, LocCountry


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocCountry
        fields = ('name', 'alpha2code')


class LocodeSerializer(serializers.ModelSerializer):

    locodecountry = serializers.StringRelatedField(many=False)
    locsubdivision = serializers.StringRelatedField(many=False)

    class Meta:
        model = Locode
        fields = ('locode', 'locname', 'locoordinates', 'locsubdivision', 'locodecountry', 'version')
