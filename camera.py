from ursina import *

app = Ursina()

cube = Entity(model = "cube", color = color.red, scale = (2,5,5))
camera.position = (-3, 0, -20)

app.run()