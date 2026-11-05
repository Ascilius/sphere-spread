from random import random
from sphere_math import *

DEBUG = True
# ROUND = 3 # number of figures after the decimal to round to

"""
n = 10
dt = 0.001 # seconds? idk
MAX_TIME = 20
output_filename = "output.csv"
"""

class Point:
	def __init__(self):
		self.r = 1.0 # radial distance from origin
		self.t = random() * pi - pi / 2 # polar angle [-pi/2, pi/2)
		self.p = random() * 2 * pi # azimuthal angle, [0, 2pi)
		
		"""
		# velocity
		self.vr = 0.0
		self.vth = 0.0
		self.vp = 0.0

		# acceleration
		self.ar = 0.0
		self.ath = 0.0
		self.ap = 0.0
		"""

		# rho is always 1 (on the surface of a unit sphere)
		# vr, ar are always 0
		# theta, vth, ath: [0, pi)
		# phi, vp, ap: [0, 2 * pi)

	def get_spherical(self):
		return (self.r, self.t, self.p)

	def get_cartesian(self):
		r = self.r
		t = self.t
		p = self.p
		return to_cartesian(r, t, p)

	def __str__(self):
		t_deg = degrees(self.t)
		p_deg = degrees(self.p)
		s = f"r: {self.r:.2f}; t: {t_deg:.2f}; p: {p_deg:.2f}"
		# string += f"\nvr: {self.vr}; vth: {round(self.vth, ROUND)}; vp: {round(self.vp, ROUND)}"
		# string += f"\nar: {self.ar}; ath: {round(self.ath, ROUND)}; vp: {round(self.ap, ROUND)}"
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

				u_ij = normalize([dx, dy, dz])

	def step(self, dt):
		self.accumulate()
		"""
		self.n += 1
		
		for point in self.points:
			# a -> v
			point.vth += point.ath * dt
			point.vp += point.ap * dt
			# v -> s
			point.theta += point.vth * dt
			point.phi += point.vp * dt
		"""

if __name__ == "__main__":
	Sphere()