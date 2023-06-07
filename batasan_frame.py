from ursina import *

def update() :
    global m
    m = m+1
    
    num_frame = 200
    
    n = m%num_frame
    if n < num_frame//2 :
        cube.x = cube.x + time.dt 
    else :
        cube.rotation_z = cube.rotation_z - time.dt*100
        
app = Ursina()
m = 0
cube = Entity(model="cube", color=color.red)
app.run()