from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Dine, DineLocation


class SelectionField(serializers.RelatedField):
    def to_internal_value(self, data):
        dine_location = DineLocation.objects.get(name=data)
        return dine_location

    def to_representation(self, value):
        return value.name


class ParticipantSerializer(serializers.ModelSerializer):
    # dine_joined = serializers.PrimaryKeyRelatedField(many=True, queryset=Dine.objects.all())  # one-to-many query

    class Meta:
        model = User
        # fields = ('id', 'username', 'dine_joined')
        fields = ('id', 'username')


class DineSerializer(serializers.ModelSerializer):
    # location = serializers.PrimaryKeyRelatedField(read_only=False,
    #                                               queryset=DineLocation.objects.all())
    location = SelectionField(read_only=False, queryset=DineLocation.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    participants = ParticipantSerializer(source='participant', many=True, read_only=True)  # many-to-many query

    class Meta:
        model = Dine
        fields = ('id', 'name', 'description', 'date', 'location', 'owner', 'participants')


class DineLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DineLocation
        fields = ('id', 'name')  # client not need id


# class JoinDineSerializer(serializers.Serializer):
#
#     def create(self, validated_data):
#         pass
#
#     def update(self, instance, validated_data):
#         username = validated_data.get('username', '')
#         print(username+"xx")
#         instance.participants = validated_data.get('')
#         return instance






