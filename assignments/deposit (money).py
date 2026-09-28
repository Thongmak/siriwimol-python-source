def deposit(money):
    print(f"ยอดเงินเริ่มต้น: {money} บาท")

    try:
        input_data = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        print()

        amount = float(input_data)

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0 ")

    except ValueError as e:
        if "could not conver" in str(e):
            print("เกิดข้อผิดพลาด: กรอกเป็นตัวอักษรไม่ได้")
        else:
            print(f"เกิดข้อผิดพลาด: {e}")

    else: 
        money_lef = money + amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {money_lef:.2f} บาท")

    finally:
        print("สิ้นสุดรายการฝากเงิน")

deposit(1000)