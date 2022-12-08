class right_angle_triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def perimeter(self):
        print("The perimeter of the triangle is",self.a+self.b+self.c)
    def semiperimeter(self):
        print("The semiperimeter of the triangle is",0.5*(self.a+self.b+self.c))
    def area(self):
        print("The area of the right angled triangle is",0.5 * self.a * self.b)            

right_angle_triangle(2,3,4).perimeter()        
right_angle_triangle(2,3,4).semiperimeter()        
right_angle_triangle(2,3,4).area()        