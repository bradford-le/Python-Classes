# Example for overwriting default output method for class objects

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
my_point = Point3D(1, 2, 3)
print my_point

# Will Output (1,2,3) rather than having to use my_point.x / my_point.y / my_point.z