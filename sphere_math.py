from math import *

DEBUG = True

"""
# angle between vectors
def vector_angle(v1, v2):
	x1 = v1[0]
	y1 = v1[1]
	z1 = v1[2]
	x2 = v2[0]
	y2 = v2[1]
	z2 = v2[2]
	return acos(x1 * x2 + y1 * y2 + z1 * z2)

# vector cross product
def cross_product(v1, v2):
	x1 = v1[0]
	y1 = v1[1]
	z1 = v1[2]
	x2 = v2[0]
	y2 = v2[1]
	z2 = v2[2]
	return [y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2]

# vector difference; subtracts v1 from v2
def sub(v1, v2)
	x1 = v1[0]
	y1 = v1[1]
	z1 = v1[2]
	x2 = v2[0]
	y2 = v2[1]
	z2 = v2[2]
	return [x2 - x1, y2 - y1, z2 - z1]

# convert to unit vector
def normalize(v):
	x = v[0]
	y = v[1]
	z = v[2]
	m = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
	return [x / m, y / m, z / m]

# negate vector
def negate_vector(v):
	return [v[0] * -1, v[1] * -1, v[2] * -1]
"""

# converts spherical coordinates to cartesian coordinates
# r: radius of the sphere
# t: angle from the x-y plane
# p: angle from the x-axis about the z-axis
def to_cartesian(r, t, p):
	x = r * cos(t) * cos(p)
	y = r * sin(t)
	z = r * cos(t) * sin(p)
	if DEBUG:
		print(f"DEBUG: x = {x}, y = {y}, z = {z}")
	return x, y, z

# calculates the angle between two spherical coordinates
def angle_between(r, t1, p1, t2, p2):
	x1, y1, z1 = to_cartesian(r, t1, p1)
	x2, y2, z2 = to_cartesian(r, t2, p2)
	
	dx = x2 - x1
	dy = y2 - y1
	dz = z2 - z1
	d = sqrt(dx * dx + dy * dy + dz * dz)

	ha = asin(d / 2 / r)
	return ha * 2

# ----------------------------------------------------------------
# tests

def test_cartesian(r, t, p):
	print(f"\nr = {r:.2f}, t = {t:.2f}, p = {p:.2f}")
	x, y, z = to_cartesian(r, t, p)
	print(f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

def test_a_between(r, t1, p1, t2, p2):
	print(f"\nr = {r:.2f}, t1 = {t1:.2f}, p1 = {p1:.2f}, t2 = {t2:.2f}, p2 = {p2:.2f}")
	t = angle_between(r, t1, p1, t2, p2)
	print(f"t = {t:.2f}")

if __name__ == "__main__":
	from random import random

	print("\nto_cartesian:")

	r = 1.0
	t = 0.0
	p = 0.0
	test_cartesian(r, t, p) # 1, 0, 0

	r = 1.0
	t = 0.0
	p = pi
	test_cartesian(r, t, p) # -1, 0, 0

	r = 1.0
	t = 0.0
	p = pi / 2
	test_cartesian(r, t, p) # 0, 1, 0

	r = 1.0
	t = 0.0
	p = pi / -2
	test_cartesian(r, t, p) # 0, -1, 0

	r = 1.0
	t = pi / 2
	p = random() * 2 * pi
	test_cartesian(r, t, p) # 0, 0, 1

	r = 1.0
	t = pi / -2
	p = random() * 2 * pi
	test_cartesian(r, t, p) # 0, 0, -1

	print("\nangle_between:")

	r = 1.0
	t1 = 0.0
	p1 = 0.0
	t2 = 0.0
	p2 = pi
	test_a_between(r, t1, p1, t2, p2) # 3.14

	r = 1.0
	t1 = pi / 4
	p1 = 0.0
	t2 = pi / -4
	p2 = pi
	test_a_between(r, t1, p1, t2, p2) # 3.14

	r = 1.0
	t1 = pi / 4
	p1 = 0.0
	t2 = pi / -8
	p2 = pi
	test_a_between(r, t1, p1, t2, p2) # 2.75

	while True:
		input()
		r = 1.0
		t1 = random() * pi - pi / 2
		p1 = random() * 2 * pi
		t2 = random() * pi - pi / 2
		p2 = random() * 2 * pi
		test_a_between(r, t1, p1, t2, p2)