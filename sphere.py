from random import random
from sphere_math import *

DEBUG = True
# ROUND = 3 # number of figures after the decimal to round to

"""
n_points = 10
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

	def get_coordinates(self):
		return (self.r, self.t, self.p)

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

	"""
	# force accumulation
	def accumulate(self):
		for i in range(self.n_points):
			point_i = self.points[i]
			s1 = to_cartesian(point_i.get_position())
			
			for j in range(i + 1, self.n_points):
				point_j = self.points[j]
				s2 = to_cartesian(point_j.get_position())
				
				# angle separation
				x1, y1, z1 = s1
				x2, y2, z2 = s2

				theta = vector_angle([x1,y1,z1],[x2,y2,z2])
				deg = theta * 180 / pi

				# force/acceleration
				a = 1 / pow(theta, 2) # mass is 1 i guess
				if DEBUG: # 					 v radians			 v degrees			v accel. factor
					print(f"DEBUG: {i} <-> {j}: {round(theta, 3)} / {round(deg, 1)} -> {round(a, 1)}")
				
				# direction calculations
				v1 = [x1,y1,z1]
				v2 = [x2,y2,z2]
				v3 = sub(v1, v2)
				u3 = normalize(v3)
				neg_u3 = negate_vector(v3) # still in cartesian

				# accumulation
				sph_theta = atan(u3[1] / u3[0])
				if u4[0] < 0:
					sph_theta += 180
				sph_u4 = [1.0, sph_theta, acos(u4[2] / 1)] # converting to spherical (TOFIX)
				sph_theta = atan(neg_u5[1] / neg_u5[0])
				if neg_u5[0] < 0:
					sph_theta += 180
				sph_neg_u5 = [1.0, sph_theta, acos(neg_u5[2] / 1)]
				
				point_i.ath = sph_u4[1]
				point_i.ap = sph_u4[2]
				point_j.ath = sph_neg_u5[1]
				point_j.ap = sph_neg_u5[2]

	def step(self, dt):
		self.accumulate()
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