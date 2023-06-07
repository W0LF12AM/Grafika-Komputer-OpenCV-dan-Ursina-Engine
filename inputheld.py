from ursina import *

def update() :
    if held_keys['r'] :
        cube.rotation_y = cube.rotation_y   + time.dt*100
    
app = Ursina()
cube = Entity(model='cube', color=color.red, scale=2)

app.run()