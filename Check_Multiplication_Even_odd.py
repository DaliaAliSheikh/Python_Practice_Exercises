"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين ويضربهما،
ثم يطبع الناتج ويفحص ما إذا كان الحاصل رقماً زوجياً أم فردياً.
"""

def multiply_numbers():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number * second_number

multiplication_result = multiply_numbers()
print(multiplication_result)

if multiplication_result % 2 == 0:
    print("رقم زوجي")
else:
    print("رقم فردي")
