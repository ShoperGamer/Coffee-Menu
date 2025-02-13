#เพิ่มข้อมูลเมนูเครื่องดื่มและราคา
menu = {"กาแฟ": 50,"ชาเขียว": 40,"โกโก้": 45}

#ฟังก์ชันสำหรับรับคำสั่งซื้อจากลูกค้า
def input_order():
    orders = {}  #เก็บข้อมูลคำสั่งซื้อของลูกค้า
    while True:

        #รับชื่อเครื่องดื่มจากผู้ใช้
        drink = input("กรุณาเลือกเครื่องดื่ม (กาแฟ, ชาเขียว, โกโก้): " ) #ชื่อเครื่องดื่ม
        if drink not in menu:
            print("ไม่มีเครื่องดื่มนี้ในเมนู กรุณาเลือกใหม่") #ป้องกันคนกรอกเมนูอื่นๆ
            continue

        #รับจำนวนแก้วจากผู้ใช้
        try:
            x = int(input(f"จำนวนแก้วของ {drink}: ") ) #รับข้อมูลจาก drink
            if x < 1:
                print("กรุณากรอกจำนวนแก้วมากกว่า 0")
                continue
        except ValueError: #ตรวจสอบว่าเป็นตัวเลขหรือไม่
            print("กรุณากรอกจำนวนเป็นตัวเลข")
            continue

        # เพิ่มรายการใน orders
        if drink in orders:
            orders[drink] += x #ถ้าใช้ใส่ +=
        else:
            orders[drink] = x #ถ้าไม่ก็จบ

        # ถามว่าต้องการสั่งเครื่องดื่มเพิ่มหรือไม่
        more = input("ต้องการสั่งเครื่องดื่มเพิ่มหรือไม่? (y/n): ").lower()
        if more != 'y': #ไม่เอาให้หยุด loop ถ้า Yes จะไปที่ drink เพื่อกรอกข้อมูล
            break
    return orders

# ฟังก์ชันสำหรับคำนวณยอดรวม
def calculate_total(orders): #นำเข้าข้อมูลจาก Order
    total = 0
    for drink, x in orders.items(): 
        total += menu[drink] * x
    return total

# เริ่มการทำงานของโปรแกรม
print("=== ร้านกาแฟลุงพี ===") #ชื่อร้าน
print("=== กินหนึ่งที วิ่งทั้งคืน ===") #สโลแกน

# รับข้อมูลคำสั่งซื้อจากลูกค้า
orders = input_order()

# คำนวณยอดรวม
total_price = calculate_total(orders)

# แสดงผลการสั่งซื้อและยอดรวม
print("\nเครื่องดื่มทั้งหมดที่สั่ง:") #\n เว้นบรรทัด
for drink, quantity in orders.items():
    print(f"{drink} {x} แก้ว") # f คือค่าของ drink กับ x
print(f"ยอดรวมที่ต้องชำระ: {total_price} บาท")
