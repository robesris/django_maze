from django.http import HttpResponse
from django.template import Context, loader

from demo_app.models import Maze, Room
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from demo_app.serializers import MazeSerializer, RoomSerializer

def index(request):
    maze_list = Maze.objects.all()
    template = loader.get_template('demo_app/index.html')
    params = []
    for maze in maze_list:
        params.append([maze, maze.room_set.all()[0].id])
    context = Context({
        #'maze_list': maze_list,
        'params': params,
        # This is only gonna work when there's only one maze
        #'first_room': maze_list[0].room_set.all()[1].id
    })
    return HttpResponse(template.render(context))

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    template = loader.get_template('demo_app/room.html')
    context = Context({
        'room': room
    })

    return HttpResponse(template.render(context))

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    maze_list = Maze.objects.all()
    room_list = Room.objects.all()

    return Response({
        #'mazes': reverse(maze_list, request=request),
        #'rooms': reverse(room_list, request=request),
        'mazes': maze_list,
        'rooms': room_list
    })

class MazeList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of mazes.
    """
    model = Maze
    serializer_class = MazeSerializer

class MazeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single maze.
    """
    model = Maze 
    serializer_class = MazeSerializer

class RoomList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of rooms.
    """
    model = Room
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single room.
    """
    model = Room
    serializer_class = RoomSerializer
