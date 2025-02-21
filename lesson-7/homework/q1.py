import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)
    
    def dot(self, other):
        return self.x *other.x + self.y *other.y * self.z +other.z


    
    
    def __mul__(self, other):
        new_x = self.x * 3
        new_y = self.y * 3
        new_z = self.z *3
        return Vector(new_x, new_y, new_z)
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 +self.z**2)
    def normalize(self):
        return Vector (self.x / mag, self.y / mag, self.z /mag )
    
    
v1= Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = v1+ v2
v4= v2-v1
v5 = v1 *3
mag = v3.magnitude()
nor = v1.normalize()
dot = v1.dot(v2)
print(v3)
print(v1)
print(v4)
print(v5)
print(mag)
print(nor)
print(dot)