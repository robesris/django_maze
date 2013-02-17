<html>
  <head>
   <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="./underscore.js" type="text/javascript"> </script>
    <script src="./backbone.js" type="text/javascript"> </script>

    <script>
      Maze = Backbone.Model.extend({
        urlRoot: 'http://localhost:8000/r_mazes',
        initialize: function(){
          console.log("Created a new maze.");
          this.on('change:name', function(maze) {
            console.log('Changed name to ' + maze.get('name'));
          });
        },
        defaults: {
          name: 'New Maze'
        }
      });

      Room = Backbone.Model.extend({
        initialize: function(){
          console.log("Created a new room.");
          this.on('change:name', function(room) {
            alert('Changed name to ' + room.get('name'));
          });
        },
        defaults: {
          name: 'Generic New Room',
          description: 'New Room!',
          north: null,
          south: null,
          east: null,
          west: null
        }
      });
    
      /*var maze = new Maze();
      var mazeDetails = {
        name: "API-Created Maze"
      };

      maze.save(mazeDetails, {
        success: function(maze) {
          alert(maze.toJSON());
        }
      });*/

      /*var maze = new Maze({id: 1});
      maze.fetch({
        data: {
          format: 'json',
        },  
        success: function(maze) {
          console.log("SUCCESS!");
          console.log(maze.toJSON());
        },
        error: function(maze) {
          console.log("ERROR!");
          console.log(maze.toJSON());
        }
      });*/

      var mazes = new Backbone.Collection;
      mazes.url = 'http://localhost:8000/r_mazes'
      mazes.fetch({
        success: function(mazes) {
          console.log("Collection Success.");
        },
        error: function(mazes) {
          console.log("Collection Error.");
        }
      });

    </script>
   </head>

   <body>
   </body>
</html>

