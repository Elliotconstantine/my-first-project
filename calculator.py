# 1. 定义加法函数
def add(x, y):
    return x + y

# 2. 定义减法函数
def subtract(x, y):
    return x - y

# 3. 定义乘法函数
def multiply(x, y):
    return x * y

# 4. 定义除法函数
def divide(x, y):
    if y == 0:
        return "错误：除数不能为0"
    return x / y

# 5. 主程序

print("欢迎使用简单计算器！")
print("请选择操作：")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")

choice = input("请输入你的选择（1/2/3/4）：")

num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("无效的选择，请重新运行程序。")