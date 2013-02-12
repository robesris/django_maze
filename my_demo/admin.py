from django.contrib import admin
from demo_app.models import Maze
from demo_app.models import Room

class MazeAdmin(admin.ModelAdmin):
    #list_display = (['name'])
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Maze, MazeAdmin)
admin.site.register(Room, RoomAdmin)
