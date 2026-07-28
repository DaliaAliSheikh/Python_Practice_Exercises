"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين
ويرجع حاصل طرح الرقم الثاني من الأول.
"""

def subtract():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number - second_number

difference_result = subtract()
print(difference_result)
