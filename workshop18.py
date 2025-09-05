print('----------------------------------')
print('โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว')
print('----------------------------------')
pro_id = input('ป้อนรหัสสินค้า : ')
pro_name = input('ป้อนชื่อสินค้า: ')
pro_type = input('xhvoxitg4mlbo8hk F/f, W/w, M/m, K/k : ')
pro_price = float( input('ป้อนราคาสินค้า : '))
print('----------------------------------')
if pro_type == 'F' or pro_type == 'f' :
    pro_price_net = pro_price - (pro_price * 2 / 100)
    print(f'ราคาขายสินค้า {pro_name} คือ {pro_price_net:,.2f} บาท')
elif pro_type == 'W' or pro_type == 'w' :
    pro_price_net = pro_price - (pro_price * 4 / 100)
    print(f'ราคาขายสินค้า {pro_name} คือ {pro_price_net:,.2f} บาท')
elif pro_type == 'N' or pro_type == 'n' :
    pro_price_net = pro_price - (pro_price * 6 / 100)
    print(f'ราคาขายสินค้า {pro_name} คือ {pro_price_net:,.2f} บาท')
elif pro_type == 'K' or pro_type == 'k' :
    pro_price_net = pro_price - (pro_price * 10 / 100)
    print(f'ราคาขายสินค้า {pro_name} คือ {pro_price_net:,.2f} บาท')
else :
    print('คุณป้อนประเภทผิด ไม่สามารถคำนวณ เข้าใจตรงกันนะ.......!!!!')
print('----------------------------------')
