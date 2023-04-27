from ursina import *

app = Ursina() 

persegi = Entity(
    model = "cube",    
    position = (0, -1, 0), 
    color = color.rgb(255, 0, 0),
    rotation = (45, 0, 45)
)

Teks = Text(             
    text = "Ini adalah kubus berwarna merah",
    color = color.white,
    position = (-0.2, 0.1, 0)
)

app.run() 
