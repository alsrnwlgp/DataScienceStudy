# test_module.py 파일
PI = 3.141592653589793238462643383279

def number_input():
    output = input("숫자 입력> ")
    return float(output)

def get_circum(radius):
    return 2 * PI * radius

def get_area(radius):
    return PI * radius * radius

print("__name__====", __name__)

if __name__ == "__main__":
    print(get_circum(10))