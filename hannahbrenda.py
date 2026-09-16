#GROUP MEMBERS
#1. CHERISSA ITERITEKA  S25B38/045
#2. WANDWASI KEVIN JOEL M25B38/021
#3. LWANGA DARREN JORDAN S25B38/022
#4. AGABA JONATHAN      M25B38/019
#5. NAMANYA HANNAH BRENDA M25B38/043
#6. AKAMPA BILLMAX S25B38/019
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width #we stating the current object as width

        if length <= 0 or width <= 0:
            raise ValueError ("Length and width must be greater than zero")

    def is_square(self):
        return self.width == self.length #if the sides are equal then it will identify as a square.
    
    def area(self):
        return self.width * self.length #returns the area by multipying width by length
    
    def perimeter(self):
        return 2 * (self_width + self_length)
    
    def scale_factor(self, factor):
        if factor < 0:
            raise ValueError("Insert a factor greater than 0")
        self.width *=factor 
        self.length = self.length * factor 
    
    def comparing_area_size(self,other):
        if not isinstance(other, Rectangle): #Check whether other is NOT a Rectangle.
            raise TypeError("other must be a Rectangle")
    
        if self.area() > other.area():
            return "The rectangle has a larger area"
        elif self.are < other.area:
            return "The other shape has a larger area"
        else:
            return "The areas are equal"
    
    def __str__ (self):
        shape = "Square" if self.is_square() else "Rectangle"

        return (
            f"{shape}: Length = {self.length},"
            f"Witdth: {self.width}"
            f"Perimter = {self.perimeter}"
        )
    def __str__(self): #tells python how we want our output to be defined
            return f"Rectangle(width={self.width}, length={self.length})"

#DEMONSTRATION:
print("RECTANGLE TOOLKIT DEMONSTRATION")
print("-" * 40)

# Create several rectangles
rectangle1 = Rectangle(8, 6)
rectangle2 = Rectangle(6, 6)       # This is a square
rectangle3 = Rectangle(7, 2)

# Normal use
print("\nInitial rectangles:")
print(rectangle1)
print(rectangle2)
print(rectangle3)

# Check whether a rectangle is a square
print("\nSquare checks:")
print(f"Rectangle 1 is a square: {rectangle1.is_square()}")
print(f"Rectangle 2 is a square: {rectangle2.is_square()}")

# Scale rectangle 1
print("\nScaling Rectangle 1 by a factor of 2...")
rectangle1.scale_factor(3)
print(rectangle1)

# Compare areas
print("\nArea comparison:")
print(f"Rectangle 1 area: {rectangle1.area()}")
print(f"Rectangle 3 area: {rectangle3.area()}")
print(rectangle1.comparing_area_size(rectangle3))

# Demonstrate an invalid action
print("\nTesting invalid scaling factor:")
try:
    rectangle3.scale_factor(0)
except ValueError as error:
    print(f"Action refused: {error}")

# Another invalid action
print("\nTesting invalid rectangle dimensions:")
try:
    invalid_rectangle = Rectangle(-5, 10)
except ValueError as error:
    print(f"Action refused: {error}")








