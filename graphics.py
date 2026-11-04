# import time
from random import choice
from ursina import *

from sphere import *
from sphere_math import *

DEBUG = True

COLORS = [color.red, color.orange, color.yellow, color.green, color.blue, color.violet]

# N = 2
SIZE_SCALE = 0.1
# TIME_SCALE = 0.01

class SphereWrapper:
	def __init__(self, n = 3):
		self.sphere = Sphere(n)

		surface_sphere = Entity(
			model = 'sphere',
			color = color.white,
			scale = 2,
			position = (0, 0, 0)
		)

		self.points = []
		for i in range(n):
			pnt = self.sphere.points[i]
			r, t, p = pnt.get_coordinates()
			pos = to_cartesian(r, t, p)
			pnt_sph = Entity(
				model = 'sphere',
				color = choice(COLORS),
				scale = SIZE_SCALE,
				position = pos
			)
			self.points.append(pnt_sph)

	def step(self, dt):
		self.sphere.step(dt)
		
		"""
		# updating positions
		for i in range(self.sphere.n):
			pnt = self.sphere.points[i]
			pos = to_cartesian(pnt.get_position())
			pnt_sph = self.points[i]
			pnt_sph.position = pos
		"""

def draw_axis():
	pip = Pipe(path = ((0,0,0),(2,0,0)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.red)
	pip = Pipe(path = ((0,0,0),(0,2,0)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.green)
	pip = Pipe(path = ((0,0,0),(0,0,2)), thicknesses = ((.01,.01),))
	Entity(model = pip, color = color.blue)

if __name__ == "__main__":
	app = Ursina()
	spw = SphereWrapper()
	if DEBUG:
		draw_axis()
	
	"""
	def update():
		spw.step(time.dt * TIME_SCALE)
	"""

	EditorCamera()
	app.run()