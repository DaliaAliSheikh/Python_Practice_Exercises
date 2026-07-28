"""
الوصف: برنامج يضرب رقمين مدخلين من المستخدم،
ثم يصنف حاصل الضرب إلى (كبير شديد، صغيرون، أو مظبوط) بناءً على قيمته.
"""

def multiply_numbers():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number * second_number

multiplication_result = multiply_numbers()
print(multiplication_result)

if multiplication_result > 100:
    print("كبير شديد")
elif multiplication_result < 10:
    print("صغيرون")
else:
    print("مظبوط")
