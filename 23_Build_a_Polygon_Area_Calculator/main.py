import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Sets the width of the rectangle.
    def set_width(self, width):
        self.width = width

    # Sets the height of the rectangle.
    def set_height(self, height):
        self.height = height

    # Returns area (width×height).
    def get_area(self):
        return self.width * self.height

    # Returns perimeter -> 2(width+height)
    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # Returns diagonal -> sqrt(width^2+height^2)        
    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    # Returns a * pattern image of the rectangle
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        result = ''   
        for row in range(self.height):
            for column in range(self.width):
                result += '*'
            result += '\n'

        return result

    # Returns the number of times the passed in shape could fit inside the shape
    def get_amount_inside(self, shape):
        # If the input shape has any dimension bigger than the calling object, then definitely cannot fit any of those
        if shape.width > self.width or shape.height > self.height:
            return 0
        # Divide (floor division) the area of the calling object with the input shape's area
        return self.get_area() // shape.get_area()

    # String representation of Rectangle object
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # Sets side length.
    def set_width(self, side):
        self.height = side
        self.width = side

    # Sets side length.
    def set_height(self, side):
        self.height = side
        self.width = side

    # Sets side length.
    def set_side(self, side):
        self.height = side
        self.width = side

    # String representation of Square object
    def __str__(self):
        # Since width and height are equal, choose any for side
        return f'Square(side={self.width})'
