def get_bus_line():
    return input("กรุณาป้อนสายรถเมล์: ")

def check_bus_line(line):
    if line == "57":
        return "สาย 57 ไปปิ่นเกล้า บางขุนนนท์"
    elif line == "3":
        return "สาย 3 ไปสนามหลวง ลาดพร้าว"
    elif line == "71":
        return "สาย 71ไปหัวลำโพง เยาวราช"
    elif line == "56":
        return "สาย 56 ไปบางลำพู สะพานกรุงธน"
    elif line == "539":
        return "สาย 539 ไปอนุสวรีย์ชัย สามเสน"
    else:
        return "ยังไม่มีข้อมูลสายรถเมล์ที่สอบถาม"

def main():
    line = get_bus_line()
    result = check_bus_line(line)
    print(result)

if __name__ == "__main__":
    main()