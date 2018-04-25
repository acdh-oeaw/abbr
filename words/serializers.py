from rest_framework import serializers
from .models import Abbreviation


class AbbreviationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Abbreviation
        fields = "__all__"
