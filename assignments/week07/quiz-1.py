"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * (self.length * self.width)

rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30



"""
สร้างคลาส circle ที่ประยุกต์ใช้คลาส Rectangle 
ในการคำนวน พท. และเส้นรอบรูปได้
"""

class circle:

    #circle ต้องใช้ข้อมูลอะไรบ้าง เพื่อคำนวน พท. และเส้นรอบรูป
    def __init__(self, length, width):
        """
        self.length = length
        self.width = width
        """
        self.radius = radius
        diameter = 2 * radius
        self.rect = Rectangle(diameter, diameter)

    # Method to get the arwa สูตรเดิมได่ไหม
    def __init__(self):
       # return self.length * self.width
        return self.rect.get_area() * (math.pi / 4)
    
    # Method to get the area สูตรเดิมได้มั้ย
    def get_area(self):
        #return 2 * (self.length + self.width)
        return self.rect.get_perimeter() * (math.pi / 4)
    
"""
myCircle = circle(....)
print(myCircle.get_area())
print(myCircle.get_perimeter())
"""
myCircle = circle(7)  
print("Circle Area:", myCircle.get_area())         
print("Circle Perimeter:", myCircle.get_perimeter())
    