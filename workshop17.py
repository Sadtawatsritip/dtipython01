from datetime import datetime

print('-------------------------------')
print('    โปรแกรมตรวจอายุยยยยยยยยย    ')
print('-------------------------------')

your_name = input('ป้อนชื่อ ==>> ')
your_yearborn = int( input('ป้อนปีเกิด (พ.ศ.) ==>>'))
print('-------------------------------')
your_ago = (datetime.now().year + 543 ) -your_yearborn

if your_ago >= 55 :
    print('คุณ {} อายุ {} ปี อายุเยอะแล้วนะ'.format(your_name, your_ago))
    print('นอนโลงไหม')
else :  
    print('คุณ {} อายุ {} ปี ยังเด็กอยุ่เลย'.format(your_name, your_ago))
    print('เด็กจัง')
print('-------------------------------')