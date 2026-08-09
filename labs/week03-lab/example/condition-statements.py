# Simple if statement
age = int(input("Enter your age: "))  #รับค่าจากผู้ใช้
if age >= 18:                         #ถ้าผ่านเงื่อนไข
    print("You are an adult")         #ปริ้นค่า

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# if-elif-else statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
