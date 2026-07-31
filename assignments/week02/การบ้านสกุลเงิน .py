print("select conversion direction: ")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter choice (1 or 2): ")

amount = float(input("Enter amount to convert: "))

rate = 35.5

if choice == '2':
    result = amount / rate
    print(f"Formula: {amount:.2f} THB / {rate} = {result:.2f} USD")
    print(f"Result: {result:.2f} USD")

elif choice == '2':
    result = amount * rate
    print(f"Fomula: {amount:.2f} USD * {rate} = {result:.2} THB")
    print(f"Result: {result:.2f} THB")

else:
    print("Invalid choice! ")