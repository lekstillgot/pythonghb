# สร้างตัวแปรเก็บข้อมูลชนิดต่างๆ
a = 10
b = 3.14
c = "Hello"
print(a)
print(b)
print(c)

# แสดงชนิดข้อมูล
print(type(a))
print(type(b))
print(type(c))


# ข้อมูลต่างชนิดสามารถบวกลบกันได้
print(a+b)

#แปลงชนิดข้อมูล
print(int(b))
print(float(a))

#ิboolean
status = True
msg =False

print(status)
print(msg)
print(type(status))

#True == 1 False == 0
print(status==1)
print(msg==0)

#การแสดงผลตัวแปรร่วมกับข้อความ

price = 200.50
qty = 5
#ตัวอย่าง
print ("ราคาสินค้า",qty,"ชิ้น",price,"บาท")

#
print("ราคาสินค้า %.2f บาท จำนวน %d ชิ้น"% (price,qty))

# 3
print(f"ราคาสินค้า {price:.2f} บาท จำนวน {qty} ชิ้น")