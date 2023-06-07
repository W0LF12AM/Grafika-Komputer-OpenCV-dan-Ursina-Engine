from ursina import *

def update() :
    cube.x = cube.x + time.dt
    camera.position = (cube.x, 0, -20) 

app = Ursina()

cube = Entity(model = "cube", color = color.red, scale = (2,5,5))
cube_2 = Entity(model = "cube", color = color.white, scale = (2,5,5))

app.run()
