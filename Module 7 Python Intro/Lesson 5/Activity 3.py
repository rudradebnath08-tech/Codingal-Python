def rectangle_area(length, breadth):
    return length * breadth

def circle_area(radius):
    return 3.14 * radius * radius

def triangle_area(base, height):
    return 0.5 * base * height

print("Area of a rectangle: ")
l = int(input("Enter length of rectangle : "))
b = int(input("Enter breadth of rectangle : "))
print("Area(Rectangle) = ", rectangle_area(l, b))

print("Area of a Circle: ")
r = int(input("Enter radius of the circle: "))
print("Area(Circle) = ", circle_area(r))

print("Area of a triangle: ")
b = int(input("Enter base of the triangle: "))
h = int(input("Enter height of the triangle : "))
print("Area(Triangle) = ", triangle_area(b, h))
