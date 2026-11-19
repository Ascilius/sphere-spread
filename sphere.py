from random import random
from sphere_math import *

DEBUG = False

class Point:
	def __init__(self):
		r = 1.0 # radial distance from origin
		t = random() * pi - pi / 2 # polar angle [-pi/2, pi/2)
		p = random() * 2 * pi # azimuthal angle, [0, 2pi)

		# if DEBUG:
		# 	print(f"DEBUG: r = {r:.2f}, t = {degrees(t):.2f}, p = {degrees(p):.2f}")

		self.sx, self.sy, self.sz = to_cartesian(r, t, p)

		self.vx = 0.0
		self.vy = 0.0
		self.vz = 0.0

		self.ax = 0.0
		self.ay = 0.0
		self.az = 0.0

	def get_spherical(self):
		r, t, p = to_spherical(self.sx, self.sy, self.sz)
		return r, t, p

	def get_cartesian(self):
		return self.sx, self.sy, self.sz

	def accumulate(self, ax, ay, az):
		self.ax += ax
		self.ay += ay
		self.az += az

	def step(self, dt):
		self.vx += self.ax * dt
		self.vy += self.ay * dt
		self.vz += self.az * dt

		x = self.sx + self.vx * dt
		y = self.sy + self.vy * dt
		z = self.sz + self.vz * dt

		self.ax = 0
		self.ay = 0
		self.az = 0

		self.sx, self.sy, self.sz = normalize(x, y, z)

	def __str__(self):
		r, t, p = self.get_spherical()
		t_deg = degrees(t)
		p_deg = degrees(p)
		s = f"r: {r:.2f}; t: {t_deg:.2f}; p: {p_deg:.2f}"
		return s

class Sphere:
	def __init__(self, n = 3):
		self.n = n

		# generation
		points = []
		for i in range(self.n):
			p = Point()
			points.append(p)
		self.points = points

		if DEBUG:
			print("DEBUG: points:")
			for i in range(n):
				p = self.points[i]
				print(f"point {i}: {p}")

	# force accumulation
	def accumulate(self):
		for i in range(self.n - 1):
			p_i = self.points[i]
			c_i = p_i.get_cartesian()
			for j in range(i + 1 , self.n):
				p_j = self.points[j]
				c_j = p_j.get_cartesian()
				
				F = force_between(c_i, c_j)

				if DEBUG:
					print(f"DEBUG: {i} <-> {j}: {F}")

				x_i, y_i, z_i = c_i
				x_j, y_j, z_j = c_j
				
				dx = x_j - x_i
				dy = y_j - y_i
				dz = z_j - z_i

				u_ij = normalize(dx, dy, dz)
				ax = u_ij[0] * F
				ay = u_ij[1] * F
				az = u_ij[2] * F

				p_j.accumulate(ax, ay, az)
				p_i.accumulate(-ax, -ay, -az)

	def step(self, dt):
		self.accumulate()
		for p in self.points:
			p.step(dt)

	def add_point(self):
		new_point = Point()
		self.points.append(new_point)
		self.n += 1
		return new_point

	def del_point(self, i):
		if i < 0 or self.n <= i:
			return
		p = self.points.pop(i)
		del(p)
		self.n -= 1

if __name__ == "__main__":
	Sphere()