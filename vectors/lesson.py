from Vector import Vector

# Addition
v1 = Vector([8.218, -9.341])
v2 = Vector([-1.129, 2.111])
print ''
print 'Addition'
print v1.plus(v2)

# Subtraction
v1 = Vector([7.119, 8.215])
v2 = Vector([-8.223, 0.878])
print ''
print 'Subtraction'
print v1.minus(v2)

# Scalar Multiplication
s = 7.41
v = Vector([1.671, -1.012, -0.318])
print ''
print 'Scalar Multiplication'
print v.times_scalar(s)

# Magnitude
print ''
print 'Magnitude'
v = Vector([-0.221, 7.437])
print format(v.magnitude(), '.5f')
v = Vector([8.813, -1.331, -6.247])
print format(v.magnitude(), '.5f')

# Normalize
print ''
print 'Normalize'
v = Vector([5.581, -2.136])
print v.normalized()
v = Vector([1.996, 3.108, -4.554])
print v.normalized()

# Dot Product
print ''
print 'Dot Product'
v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
print v1.dot_product(v2)
v1 = Vector([-5.955, -4.904, -1.874])
v2 = Vector([-4.496, -8.755, 7.103])
print v1.dot_product(v2)

# Angles
v1 = Vector([3.183, -7.627])
v2 = Vector([-2.668, 5.319])
print ''
print 'Angle Radians'
print v1.angle_radians(v2)
print v1.angle_with(v2, False)
v1 = Vector([7.35, 0.221, 5.188])
v2 = Vector([2.751, 8.259, 3.985])
print ''
print 'Angle Degrees'
print v1.angle_degrees(v2)
print v1.angle_with(v2, True)

# Parallel & Orthogonal
print ''
print 'Parallel & Orthogonal'
v1 = Vector([-7.579, -7.88])
v2 = Vector([22.737, 23.64])
print v1
print v2
print 'Parallel: {}'.format(v1.parallel_with(v2))
print 'Orthogonal: {}'.format(v1.orthogonal_with(v2))
print ''
v1 = Vector([-2.029, 9.97, 4.172])
v2 = Vector([-9.231, -6.639, -7.245])
print v1
print v2
print 'Parallel: {}'.format(v1.parallel_with(v2))
print 'Orthogonal: {}'.format(v1.orthogonal_with(v2))
