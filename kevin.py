#GROUP MEMBERS
#1. CHERISSA ITERITEKA  S25B38/045
#2. WANDWASI KEVIN JOEL M25B38/021
#3. LWANGA DARREN JORDAN S25B38/022
#4. AGABA JONATHAN      M25B38/019
#5. NAMANYA HANNAH BRENDA M25B38/043
#6. AKAMPA BILLMAX S25B38/019
class Rectangle:
    """Represents a rectangular shape used in layout calculations."""

    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be greater than zero.")

        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def is_square(self):
        """Return True if the rectangle is a square."""
        return self.length == self.width

    def scale(self, factor):
        """Scale both dimensions by a positive factor."""
        if factor <= 0:
            raise ValueError("Scaling factor must be greater than zero.")

        self.length *= factor
        self.width *= factor

    def compare_area(self, other):
        """Compare the area of this rectangle with another rectangle."""
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare areas with another Rectangle.")

        if self.area() > other.area():
            return "This rectangle has the larger area."
        elif self.area() < other.area():
            return "The other rectangle has the larger area."
        else:
            return "The rectangles have equal areas."

    def __str__(self):
        """Return a useful description of the rectangle."""
        shape = "Square" if self.is_square() else "Rectangle"

        return (
            f"{shape}: Length = {self.length}, "
            f"Width = {self.width}, "
            f"Area = {self.area()}, "
            f"Perimeter = {self.perimeter()}"
        )


# --------------------------------------------------
# DEMONSTRATION
# --------------------------------------------------

print("RECTANGLE TOOLKIT DEMONSTRATION")
print("-" * 40)

# Create several rectangles
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 8)       # This is a square
rectangle3 = Rectangle(6, 4)

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
rectangle1.scale(2)
print(rectangle1)

# Compare areas
print("\nArea comparison:")
print(f"Rectangle 1 area: {rectangle1.area()}")
print(f"Rectangle 3 area: {rectangle3.area()}")
print(rectangle1.compare_area(rectangle3))

# Demonstrate an invalid action
print("\nTesting invalid scaling factor:")
try:
    rectangle3.scale(0)
except ValueError as error:
    print(f"Action refused: {error}")

# Another invalid action
print("\nTesting invalid rectangle dimensions:")
try:
    invalid_rectangle = Rectangle(-5, 10)
except ValueError as error:
    print(f"Action refused: {error}")