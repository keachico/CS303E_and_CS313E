import math

class Circle:
    """Define a class of circles. Circles have an associated radius."""
    _circlesCount = 0

    def printCount():
        print("Created " + str( Circle._circlesCount ) + " circles.")
        
    def __init__(self, radius):
        self._radius = radius
        Circle._circlesCount += 1
        
    def __str__(self):
        return "Circle with radius " + str(self._radius)
    
    def circumference(self):
        return 2 * math.pi * self._radius

    def area(self):
        return math.pi * (self._radius ** 2)
