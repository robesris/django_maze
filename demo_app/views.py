from django.http import HttpResponse
from django.template import Context, loader

from demo_app.models import Maze, Room

def index(request):
    maze_list = Maze.objects.all()
    template = loader.get_template('demo_app/index.html')
    context = Context({
        'maze_list': maze_list,

        # This is only gonna work when there's only one maze
        'first_room': maze_list[0].room_set.all()[1].id
    })
    return HttpResponse(template.render(context))

def room(request, room_id):
    room = Room.objects.get(id=room_id)
    template = loader.get_template('demo_app/room.html')
    context = Context({
        'room': room
    })

    return HttpResponse(template.render(context))
