# surface volume = pi * r * r * h
# area = 2*pi*r*h+2*pi*r*r

radius = int(input("Enter Radius of Cylinder:"))
height = int(input("Enter Height of Cylinder"))

volume = 3.14*radius*radius*height
area = 2*3.14*radius*height+2*3.14*radius*radius

print("Surface volume of Cylinder is:",volume)
print("Area of Cylinder is:",area)
