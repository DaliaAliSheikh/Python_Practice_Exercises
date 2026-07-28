"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين
ويرجع حاصل طرح الرقم الثاني من الأول.
"""

def subtract():
    num1 = float(input("enter the first number :"))
    num2 = float(input("enter the second number :"))
    return num1 - num2

difference_result = subtract()
print(difference_result)
