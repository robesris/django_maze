from django.contrib.auth.models import User, Group, Permission
from demo_app.models import Maze, Room
from rest_framework import serializers

class MazeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maze
        fields = ('url', 'name', 'created_date')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.ManySlugRelatedField(
        slug_field='codename',
        queryset=Permission.objects.all()
    )

    class Meta:
        model = Room
        fields = ('url', 'maze', 'name', 'description', 'north', 'south', 'east', 'west')
