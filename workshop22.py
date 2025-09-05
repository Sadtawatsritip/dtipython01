print('-------------------------------')
print('    โปรแกรมแสดงข้อความต้อนรับนักศึกษา')
print('-------------------------------')
name = input("กรุณาป้อนชื่อนักศึกษา: ")
year = input("กรุณาป้อนชั้นปี (ตัวเลข): ")
if year == "1":
    print("Welcome Freshman")
elif year == "2":
    print("Welcome Sophomore")
elif year == "3":
    print("Welcome Junior")
elif year == "4":
    print("Welcome Senior")
else:
    print("Oh, no ....")