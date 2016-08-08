from math import sqrt, acos, pi, degrees
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        formatted_coordinates = [format(x, '.6f') for x in self.coordinates]
        joined_list = ', '.join(formatted_coordinates)
        return 'Vector: ({})'.format(joined_list)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        # new_coordinates = []
        # for i in range(self.dimension):
        #     new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)


    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        # new_coordinates = []
        # for i in range(self.dimension):
        #     new_coordinates.append(self.coordinates[i] - v.coordinates[i])
        return Vector(new_coordinates)


    def times_scalar(self, s):
        new_coordinates = [Decimal(s)*x for x in self.coordinates]
        # new_coordinates = []
        # for i in range(self.dimension):
        #     new_coordinates.append(Decimal(s) * self.coordinates[i])
        return Vector(new_coordinates)


    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        # coordinates_squared = []
        # for i in range(self.dimension):
        #     coordinates_squared.append(self.coordinates[i]**2)
        return Decimal(sqrt(sum(coordinates_squared)))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0)/magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def dot_product(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        # new_coordinates = []
        # for i in range(self.dimension):
        #     new_coordinates.append(self.coordinates[i] * v.coordinates[i])
        # return sum(new_coordinates)


    def angle_radians(self, v):
        dot_product = self.dot_product(v)
        return acos(dot_product/(self.magnitude() * v.magnitude()))

    
    def angle_degrees(self, v):
        return degrees(self.angle_radians(v))


    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_radians = acos(u1.dot_product(u2))

            if in_degrees:
                return degrees(angle_radians)
            else:
                return angle_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e


    def parallel_with(self, v):
        check_list = [x/y for x,y in zip(self.coordinates, v.coordinates)]
        return all(x==check_list[0] for x in check_list)


    def orthogonal_with(self, v):
        if (self.dot_product(v) == 0.0):
            return True
        else:
            return False
