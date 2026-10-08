import math
import random

DEBUG = False

n_points = 10
dt = 0.001 # seconds? idk
MAX_TIME = 20
output_filename = "output.csv"

class Point:
	__init__(self):
		# position
		self.rho = 1.0 # radial distance from origin
		self.theta = random.random() * 2 * math.pi # polar angle
		self.phi = random.random() * 2 * math.pi # azimuthal angle
		
		# velocity
		self.vr = 0.0
		self.vth = 0.0
		self.vp = 0.0

		# acceleration
		self.ar = 0.0
		self.ath = 0.0
		self.ap = 0.0

		# rho is always 1 (on the surface of a unit sphere)
		# vr, ar are always 0
		# rest are [0, 2 * pi)

class Sphere:
	__init__(self, n_points):
		self.n_points = n_points
		self.n = 0

		# generation
		self.points = [] # [rho (should always be 1), theta, phi, vr (should always be 0), vth, vp, ar (should always be 0), ath, ap]

		for i in range(self.n):
			self.points.append([1.0, random.random() * 2 * math.pi, random.random() * 2 * math.pi, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	# force accumulation
	def accumulate(self):
		for i in range(self.n_points):
			r1 = points[i][0] # getting coords
			t1 = points[i][1]
			p1 = points[i][2]
			
			for j in range(i + 1, self.n_points):
				r2 = points[j][0]
				t2 = points[j][1]
				p2 = points[j][2]
				
				# angle separation
				x1 = r1 * math.sin(p1) * math.cos(t1) # x = (rho)sin(phi)cos(theta)
				y1 = r1 * math.sin(p1) * math.sin(t1) # y = (rho)sin(phi)sin(theta)
				z1 = r1 * math.cos(p1)				  # z = (rho)cos(phi)

				x2 = r2 * math.sin(p2) * math.cos(t2)
				y2 = r2 * math.sin(p2) * math.sin(t2)
				z2 = r2 * math.cos(p2)

				theta = vector_angle([x1,y1,z1],[x2,y2,z2])
				deg = theta * 180 / math.pi

				# force/acceleration
				a = 1 / math.pow(theta, 2) # mass is 1 i guess
				if DEBUG:
					print(f"{i} <-> {j}: {round(theta, 3)} / {round(deg, 1)} -> {round(a, 1)}")
				
				# direction calculations
				v1 = [x1,y1,z1]
				v2 = [x2,y2,z2]
				v3 = cross_product(v1,v2)
				v4 = cross_product(v1,v3)
				u4 = normalize(v4) # see paper notes
				v5 = cross_product(v2,v3)
				neg_u5 = negate_vector(normalize(v5)) # still in cartesian

				# accumulation
				sph_theta = math.atan(u4[1] / u4[0])
				if u4[0] < 0:
					sph_theta += 180
				sph_u4 = [1.0, sph_theta, math.acos(u4[2] / 1)] # converting to spherical (TOFIX)
				sph_theta = math.atan(neg_u5[1] / neg_u5[0])
				if neg_u5[0] < 0:
					sph_theta += 180
				sph_neg_u5 = [1.0, sph_theta, math.acos(neg_u5[2] / 1)]
				
				points[i][7] = sph_u4[1]
				points[i][8] = sph_u4[2]
				points[j][7] = sph_neg_u5[1]
				points[j][8] = sph_neg_u5[2]

		def step(self):
			self.accumulate()
			
			for point in points:
				# a -> v
				point[4] += point[7] * dt
				point[5] += point[8] * dt
				# v -> s
				point[1] += point[4] * dt
				point[2] += point[5] * dt

			self.n += 1


if __name__ == "__main__":
	# setup
	MAX_FRAMES = MAX_TIME / dt
	output_file = open(output_filename, "w")

	# generation
	self.points = [] # [rho (should always be 1), theta, phi, vr (should always be 0), vth, vp, ar (should always be 0), ath, ap]

	for i in range(self.n):
		self.points.append([1.0, random.random() * 2 * math.pi, random.random() * 2 * math.pi, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

	# physics loop
	n = 0
	while True:
		n += 1
		if DEBUG:
			print(f"Frame {n}:\n")
			print("[rho, theta, phi, vr, vth, vp, ar, ath, ap]")
			for point in points:
				print(point)

		# force accumulation
		angles = []
		for i in range(n_points):
			if DEBUG:
				print()
			r1 = points[i][0] # getting coords
			t1 = points[i][1]
			p1 = points[i][2]
			for j in range(i + 1, n_points):
				r2 = points[j][0]
				t2 = points[j][1]
				p2 = points[j][2]
				
				# angle separation
				x1 = r1 * math.sin(p1) * math.cos(t1) # x = (rho)sin(phi)cos(theta)
				y1 = r1 * math.sin(p1) * math.sin(t1) # y = (rho)sin(phi)sin(theta)
				z1 = r1 * math.cos(p1)				  # z = (rho)cos(phi)

				x2 = r2 * math.sin(p2) * math.cos(t2)
				y2 = r2 * math.sin(p2) * math.sin(t2)
				z2 = r2 * math.cos(p2)

				theta = vector_angle([x1,y1,z1],[x2,y2,z2])
				angles.append(theta) # for statistics
				deg = theta * 180 / math.pi

				# force/acceleration
				a = 1 / math.pow(theta, 2) # mass is 1 i guess
				if DEBUG:
					print(f"{i} <-> {j}: {round(theta, 3)} / {round(deg, 1)} -> {round(a, 1)}")
				"""
				else:
					print(f"{i} <-> {j}: {round(deg, 1)}")
				"""

				# direction calculations
				v1 = [x1,y1,z1]
				v2 = [x2,y2,z2]
				v3 = cross_product(v1,v2)
				v4 = cross_product(v1,v3)
				u4 = normalize(v4) # see paper notes
				v5 = cross_product(v2,v3)
				neg_u5 = negate_vector(normalize(v5)) # still in cartesian
				if DEBUG:
					print("v1:", v1)
					print("v2:", v2)
					print("v3:", v3)
					print(f"v4: {v4}; u4: {u4} ({math.sqrt(math.pow(u4[0], 2) + math.pow(u4[1], 2) + math.pow(u4[2], 2))}) ({round(vector_angle(v1, u4) * 180 / math.pi, 1)})")
					print(f"v5: {v5}; -u5: {neg_u5} ({math.sqrt(math.pow(neg_u5[0], 2) + math.pow(neg_u5[1], 2) + math.pow(neg_u5[2], 2))}) ({round(vector_angle(v2, neg_u5) * 180 / math.pi, 1)})")

				# accumulation
				sph_theta = math.atan(u4[1] / u4[0])
				if u4[0] < 0:
					sph_theta += 180
				sph_u4 = [1.0, sph_theta, math.acos(u4[2] / 1)] # converting to spherical (TOFIX)
				sph_theta = math.atan(neg_u5[1] / neg_u5[0])
				if neg_u5[0] < 0:
					sph_theta += 180
				sph_neg_u5 = [1.0, sph_theta, math.acos(neg_u5[2] / 1)]
				if DEBUG:
					print("sph_u4:", sph_u4)
					print("sph_neg_u5:", sph_neg_u5)
				points[i][7] = sph_u4[1]
				points[i][8] = sph_u4[2]
				points[j][7] = sph_neg_u5[1]
				points[j][8] = sph_neg_u5[2]

		# statistics / data collection
		n_angles = len(angles)
		
		mean = 0
		for angle in angles:
			mean += angle
		mean /= n_angles
		
		variance = 0
		for angle in angles:
			variance += pow(angle - mean, 2)
		variance /= n_angles
		
		stdev = math.sqrt(variance)

		if DEBUG:
			print(f"Statistics:\n{angles} ({n_angles})")
			print("Mean:", mean)
			print("Variance:", variance)
			print("Standard deviation:", stdev)
		else:
			print(f"{n}: {stdev}")
			output_file.write(str(n) + ", " + str(stdev) + "\n")
		if (n == MAX_FRAMES):
			print(f"Data written to \"{output_filename}\"; Done!")
			output_file.close()
			exit()

		# stepping
		if DEBUG:
			input()
		for point in points:
			# a -> v
			point[4] += point[7] * dt
			point[5] += point[8] * dt
			# v -> s
			point[1] += point[4] * dt
			point[2] += point[5] * dt