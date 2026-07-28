"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين، يجمعهم،
ثم يفحص ما إذا كان الناتج يساوي 50 أم لا.
"""

def check_sum():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number + second_number

result = check_sum()
print("the result is", result)

if result == 50:
    print("right")
else:
    print("wrong")
