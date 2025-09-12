def get_number(prompt):
    return int(input(prompt))

def multiply(a, b):
    return a * b

def show_result(a, b, result):
    print(f"{a} x {b} = {result}")

def is_over_limit(result, limit=5000):
    return result > limit

def main():
    while True:
        num1 = get_number("ป้อนตัวเลขที่ 1: ")
        num2 = get_number("ป้อนตัวเลขที่ 2: ")
        result = multiply(num1, num2)
        show_result(num1, num2, result)
        if is_over_limit(result):
            break

if __name__ == "__main__":
    main()