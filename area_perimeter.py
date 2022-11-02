#!/usr/bin/python3
"""area perimeter"""


class Object:
    """definition of class object"""
    def __init__(self):
        """ initializes all the instance of object class module"""
        self.height = ""
        self.width = ""
        self.hyp = ""
        self.base = ""
        self.radius = ""

    def set_height(self, height):
        """setter for height"""
        self.height = height

    def set_width(self, width):
        """setter for width"""
        self.width = width

    def set_base(self, base):
        """setter for base"""
        self.base = base

    def set_radius(self, radius):
        """setter for radius"""
        self.radius = radius

    def set_hyp(self, hyp):
        """setter for Hypotenuse"""
        self.hyp = hyp

    def get_radius(self):
        return self.radius

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_hyp(self):
        return self.hyp

    def get_base(self):
        return self.base

    def rectangle(self):
        """ Calculates the area and perimeter of rectangle"""
        area = self.height * self.width
        perimeter = 2 * (self.height + self.width)
        return "The are of the rectangle is: {}\nThe perimeter of the rectangle is: {}\n".format(
            area, perimeter
        )

    def circle(self):
        """Calculates the area and perimeter of a circle"""
        area = 22 / 7 * self.radius * self.radius
        perimeter = 2 * (22/7) * self.radius
        return "The area of the circle is : {}\nThe perimeter of the circle is: {}\n".format(area, perimeter)


def main():
    """Main function"""
    value = Object()
    variables = input("enter any value numbers [Radius, Height, Base,"
                      "Hypotenuse, width] Enter any not fixed"
                      "to all of them: ").strip()
    for i in range(len(variables)):
        if i == 1:
            value.circle()
        elif i == 2:
            value.rectangle()
        else:
            print('We tried: time caught up to us')


if __name__ == "__main__":
    main()
