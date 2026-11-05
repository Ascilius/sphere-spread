from ursina import *

import time

app = Ursina()

sphere1 = Entity(
	model = 'sphere',
	color = color.white,
	scale = 1,
	position = (0, 0, 0)
)

sphere2 = Entity(
	model = 'sphere',
	color = color.white,
	scale = 1,
	position = (1, 0, 0)
)

EditorCamera()

def update():
	sphere2.x += time.dt

app.run()