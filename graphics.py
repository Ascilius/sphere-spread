# import time
from random import choice
from ursina import *

from sphere import *
from sphere_math import *

DEBUG = False

COLORS = [color.red, color.orange, color.yellow, color.green, color.blue, color.violet]

N = 6
SIZE_SCALE = 0.1
TIME_SCALE = 1.0

class SphereWrapper:
	def __init__(self, n = 3):
		self.sphere = Sphere(n)

		if DEBUG:
			surface_sphere = Entity(
				model = 'sphere',
				color = color.white,
				scale = 2,
				position = (0, 0, 0)
			)

		self.points = []
		for i in range(n):
			pnt = self.sphere.points[i]
			pos = pnt.get_cartesian()
			pnt_sph = Entity(
				model = 'sphere',
				color = choice(COLORS),
				scale = SIZE_SCALE,
				position = pos
			)
			self.points.append(pnt_sph)

	def step(self, dt):
		self.sphere.step(dt)
		
		# updating positions
		for i in range(self.sphere.n):
			pnt = self.sphere.points[i]
			pos = pnt.get_cartesian()
			pnt_sph = self.points[i]
			pnt_sph.position = pos

	def add_point(self):
		pnt = self.sphere.add_point()
		pos = pnt.get_cartesian()
		new_point = Entity(
			model = 'sphere',
			color = choice(COLORS),
			scale = SIZE_SCALE,
			position = pos
		)
		self.points.append(new_point)

	def del_point(self):
		n = self.sphere.n
		if n == 0:
			return
		i = int(random() * n)
		p = self.points.pop(i)
		destroy(p)
		self.sphere.del_point(i)

def draw_axis():
	pip = Pipe(path = ((0,0,0),(2,0,0)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.red)
	pip = Pipe(path = ((0,0,0),(0,2,0)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.green)
	pip = Pipe(path = ((0,0,0),(0,0,2)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.blue)

if __name__ == "__main__":
	app = Ursina()
	spw = SphereWrapper(N)
	if DEBUG:
		draw_axis()

	pause = True

	def input(key):
		global pause

		# if DEBUG:
		# 	print("DEBUG: key:", key)

		if key == "right arrow":
			spw.step(1 / 144 * TIME_SCALE)
		elif key == "space":
			pause = not pause
		elif key == "escape":
			application.quit()
		elif key == "=":
			spw.add_point()
		elif key == "-":
			spw.del_point()

	def update():
		global pause
		if not pause:
			spw.step(time.dt * TIME_SCALE)
	
	EditorCamera()
	app.run()