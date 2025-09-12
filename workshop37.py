def get_name():
    return input("กรุณากรอกชื่อของคุณ: ")

def get_birth_year():
    return int(input("กรุณากรอกปีเกิดของคุณ (พ.ศ.): "))

def calculate_age(birth_year, current_year=2568):
    return current_year - birth_year

def show_result(name, age):
    print(f"{name} คุณมีอายุ {age} ปี")
    if age >= 55:
        print("คุณแก่แล้ว...")
    else:
        print("คุณยังไม่แก่...")

def main():
    name = get_name()
    birth_year = get_birth_year()
    age = calculate_age(birth_year)
    show_result(name, age)

if __name__ == "__main__":
    main()