#GROUP MEMBERS
#1. CHERISSA ITERITEKA  S25B38/045
#2. WANDWASI KEVIN JOEL M25B38/021
#3. LWANGA DARREN JORDAN S25B38/022
#4. AGABA JONATHAN      M25B38/019
#5. NAMANYA HANNAH BRENDA M25B38/043
#6. AKAMPA BILLMAX S25B38/019
class Rectangle:
    def __init__(self, length, width):
        # Initialize a rectangle with given length and width
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        
        self.length = length
        self.width = width

    def area(self):
        #return the area of the rectangle
        return self.length * self.width

    def perimeter(self):
        #return the perimeter of the rectangle
        return 2 * (self.length + self.width)

    def is_square(self):
        #return whether the rectangle is a square "TRUE"
        return self.length == self.width

    def scale(self, factor):
        # Scale the rectangle by a given positive factor
        if factor <= 0:
            raise ValueError("Scaling factor must be positive and non-zero.")
        self.length *= factor
        self.width *= factor

    def compare_area(self, other):
        # Compare the area of this rectangle with another rectangle
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare with another Rectangle.")
        if self.area() > other.area():
            return "This rectangle has a larger area."
        elif self.area() < other.area():
            return "The other rectangle has a larger area."
        else:
            return "Both rectangles have equal area."

    def __str__(self):
        # Return a string representation of the rectangle
        square_status = "Square" if self.is_square() else "Rectangle"
        return f"{square_status}: {self.length} x {self.width}"


# --- DEMO SCRIPT ---
print("GEOMETRY TOOLKIT DEMO\n")
if __name__ == "__main__":
    # Create rectangles
    r1 = Rectangle(10, 5)
    r2 = Rectangle(7, 7)   # This is a square
    r3 = Rectangle(12, 8)

    # Print rectangles
    print("Rectangles:\n")

    print(r1)
    print(r2)
    print(r3)

    # Show area and perimeter
    print("Area of r1:", r1.area())
    print("Perimeter of r2:", r2.perimeter())

    # Compare areas
    print("Comparing r1 and r2:", r1.compare_area(r2))

    # Scale a rectangle
    print("\nScaling r1 by factor 2...")
    r1.scale(2)
    print(r1)

    print("\nScaling r1 by factor 0.5...")
    r1.scale(0.5)
    print(r1)

    # Attempt invalid scaling
    try:
        print("\nTrying to scale r2 by -1...")
        r2.scale(-1)
    except ValueError as e:
        print("Error:", e)
#END