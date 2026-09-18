#โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย

try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")

    result = 0 
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print(f"{num1} {operator} {num2} = {result}")
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

except ZeroDivisionError:
    print("ไม่สามารถหารตัวศูนย์ได้")

else:
    print("ทำงานได้สมบูรณ์")

finally:
    print("จบการทำงาน")