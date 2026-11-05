import math

# angle between vectors
def vector_angle(v1, v2):
	x1 = v1[0]
	y1 = v1[1]
	z1 = v1[2]
	x2 = v2[0]
	y2 = v2[1]
	z2 = v2[2]
	return math.acos(x1 * x2 + y1 * y2 + z1 * z2)

# vector cross product
def cross_product(v1, v2):
	x1 = v1[0]
	y1 = v1[1]
	z1 = v1[2]
	x2 = v2[0]
	y2 = v2[1]
	z2 = v2[2]
	return [y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2]

# convert to unit vector
def normalize(v):
	x = v[0]
	y = v[1]
	z = v[2]
	m = math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))
	return [x / m, y / m, z / m]

# negate vector
def negate_vector(v):
	return [v[0] * -1, v[1] * -1, v[2] * -1]