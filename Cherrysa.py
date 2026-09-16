# ============================================================
# GROUP 5 - GEOMETRY TOOLKIT
# Topic 5: Classes and Objects
# File Name: Group5_System.py
# ============================================================

#GROUP MEMBERS
#1. CHERISSA ITERITEKA  S25B38/045
#2. WANDWASI KEVIN JOEL M25B38/021
#3. LWANGA DARREN JORDAN S25B38/022
#4. AGABA JONATHAN      M25B38/019
#5. NAMANYA HANNAH BRENDA M25B38/043
#6. AKAMPA BILLMAX S25B38/019
class Rectangle:
    """
    A class that represents a rectangle.
    """

    def __init__(self, length, width):
        # Check that dimensions are positive
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be greater than zero.")

        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)

    def is_square(self):
        """Return True if the rectangle is a square."""
        return self.length == self.width

    def scale(self, factor):
        """
        Scale the rectangle by a given factor.
        The factor must be greater than zero.
        """
        if factor <= 0:
            raise ValueError("Scaling factor must be greater than zero.")

        self.length = self.length * factor
        self.width = self.width * factor

    def compare_area(self, other):
        """
        Compare the area of this rectangle with another rectangle.
        """
        if self.area() > other.area():
            return "This rectangle has a larger area."
        elif self.area() < other.area():
            return "The other rectangle has a larger area."
        else:
            return "Both rectangles have equal areas."

    def __str__(self):
        """Return a useful description when the object is printed."""
        shape = "Square" if self.is_square() else "Rectangle"

        return (
            f"{shape}: Length = {self.length}, "
            f"Width = {self.width}, "
            f"Area = {self.area()}, "
            f"Perimeter = {self.perimeter()}"
        )


# ============================================================
# DEMONSTRATION
# ============================================================

print("========== GROUP 5: GEOMETRY TOOLKIT ==========\n")

# Create several rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 8)       # This is a square
rectangle3 = Rectangle(6, 4)

# Print the rectangles
print("Original Rectangles:")
print(rectangle1)
print(rectangle2)
print(rectangle3)

print("\n--------------------------------------------")

# Check whether rectangle2 is a square
print("Is Rectangle 2 a square?", rectangle2.is_square())

# Scale rectangle1 by a factor of 2
print("\nScaling Rectangle 1 by a factor of 2...")
rectangle1.scale(2)

print("Rectangle 1 after scaling:")
print(rectangle1)

print("\n--------------------------------------------")

# Compare areas
print("Comparing Rectangle 1 and Rectangle 2:")
print(rectangle1.compare_area(rectangle2))

print("\nComparing Rectangle 2 and Rectangle 3:")
print(rectangle2.compare_area(rectangle3))

print("\n--------------------------------------------")

# Demonstrate an invalid action
print("Testing an invalid scaling action:")

try:
    rectangle3.scale(0)
except ValueError as error:
    print("Invalid action refused:", error)

print("\n========== END OF DEMONSTRATION ==========")