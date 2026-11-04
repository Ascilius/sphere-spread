from ursina import *

app = Ursina()

Entity(model = 'sphere', scale = 0.02) # origin

pip = Pipe(path = ((0,0,0),(1,0,0)), thicknesses = ((.01,.01),))
Entity(model = pip, color = color.red)
pip = Pipe(path = ((0,0,0),(0,1,0)), thicknesses = ((.01,.01),))
Entity(model = pip, color = color.green)
pip = Pipe(path = ((0,0,0),(0,0,1)), thicknesses = ((.01,.01),))
Entity(model = pip, color = color.blue)

EditorCamera()
app.run()