        #โจรท์
#เขียน function ชื่อ convert_currency()
#ที่ำหน้าที่แปลงสกุลเงิน
#THB <--> USD กำหนดให้ 1 USD = 33 THB
#ทั้งนี้ให้ function ดังกล่าว รับข้อมูล จำนวนเงินที่ต้องการแปล และสกุลเงินปลายทาง 

#ตัวอย่างวิธีการเรียกใช้ 
#convet_currency(100, "USD")
#convet_currency(100, "THB")

#ตัวอย่างหน้าจอ
#100 THB = 3.33 USD
#100 USD = 3300.3 THB

def convert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

convert_currency(100, "USD")
convert_currency(100, "THB")