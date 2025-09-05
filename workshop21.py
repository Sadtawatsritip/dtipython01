print('-------------------------------')
print('  โปรแกรมคำนวณค่าคอมมิชชั่นของพนักงานขาย')
print('-------------------------------')
emp_id = input("กรุณาป้อนรหัสพนักงาน: ")
emp_name = input("กรุณาป้อนชื่อพนักงาน: ")
sales = float(input("กรุณาป้อนยอดขายของพนักงาน (บาท): "))
if sales <= 1000:
    commission = 0.0
elif 1001 <= sales <= 2000:
    commission = sales * 0.01
elif 2001 <= sales <= 3000:
    commission = sales * 0.03
else:
    commission = sales * 0.05
print(f"รหัสพนักงาน: {emp_id}")
print(f"ชื่อพนักงาน: {emp_name}")
print(f"ยอดขาย: {sales:.2f} บาท")
print(f"ค่าคอมมิชชั่น: {commission:.2f} บาท")