from math import *

DEBUG = True

# convert to unit vector
def normalize(x, y, z):
	m = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
	return x / m, y / m, z / m

# negate vector
def negate_vector(v):
	return [v[0] * -1, v[1] * -1, v[2] * -1]

# converts cartesian coordinates to spherical coordinates
def to_spherical(x, y, z):
	r = sqrt(x * x + y * y + z * z)
	h = sqrt(x * x + z * z)
	t = acos(h / r)
	if y < 0:
		t *= -1
	p = atan2(z, x)
	if p < 0:
		p += 2 * pi
	return r, t, p

# converts spherical coordinates to cartesian coordinates
# r: radius of the sphere
# t: angle from the x-y plane
# p: angle from the x-axis about the z-axis
def to_cartesian(r, t, p):
	x = r * cos(t) * cos(p)
	y = r * sin(t)
	z = r * cos(t) * sin(p)
	# if DEBUG:
	# w	print(f"DEBUG: x = {x}, y = {y}, z = {z}")
	return x, y, z

# calculates the angle between two cartesian coordinates
def angle_between(r, c_i, c_j):
	x1, y1, z1 = c_i
	x2, y2, z2 = c_j
	
	dx = x2 - x1
	dy = y2 - y1
	dz = z2 - z1
	d = sqrt(dx * dx + dy * dy + dz * dz)

	ha = asin(d / 2 / r)
	return ha * 2

# calculates the force between two cartesian coordinates
def force_between(c_i, c_j):
	a = angle_between(1, c_i, c_j)
	return 1 / (a * a)

# ----------------------------------------------------------------
# tests

def test_spherical(x, y, z):
	print(f"\nx = {x:.2f}, y = {y:.2f}, z = {z:.2f}")
	r, t, p = to_spherical(x, y, z)
	print(f"r = {r:.2f}, t = {t:.2f}, p = {p:.2f}")

def test_cartesian(r, t, p):
	print(f"\nr = {r:.2f}, t = {t:.2f}, p = {p:.2f}")
	x, y, z = to_cartesian(r, t, p)
	print(f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

def test_a_between(r, t1, p1, t2, p2):
	print(f"\nr = {r:.2f}, t1 = {t1:.2f}, p1 = {p1:.2f}, t2 = {t2:.2f}, p2 = {p2:.2f}")
	c1 = to_cartesian(r, t1, p1)
	c2 = to_cartesian(r, t2, p2)
	t = angle_between(1, c1, c2)
	print(f"t = {t:.2f}")

if __name__ == "__main__":
	from random import random

	print("\nto_spherical:")

	x = 1.0
	y = 0.0
	z = 0.0
	test_spherical(x, y, z) # 1, 0, 0

	x = 0.0
	y = 1.0
	z = 0.0
	test_spherical(x, y, z) # 1, 1.57, 0

	x = 0.0
	y = 0.0
	z = 1.0
	test_spherical(x, y, z) # 1, 0, 1.57

	x = -1.0
	y = 0.0
	z = 0.0
	test_spherical(x, y, z) # 1, 0, 3.14

	x = 0.0
	y = -1.0
	z = 0.0
	test_spherical(x, y, z) # 1, -1.57, 0

	x = 0.0
	y = 0.0
	z = -1.0
	test_spherical(x, y, z) # 1, 0, 4.71

	while True:
		input()
		x = random() - 0.5
		y = random() - 0.5
		z = random() - 0.5
		x, y, z = normalize(x, y, z)
		test_spherical(x, y, z)

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