from ursina import *

def update():
    global speed
    
    Cube.x = Cube.x + time.dt * speed
    if abs (Cube.x) > 3 : 
        speed = speed * -1

app = Ursina()
speed = 1
Cube = Entity(model="cube", color = color.red)
app.run()