"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين ويجمعهما،
ويكرر العملية 3 مرات مع تصنيف الناتج (تقيل، مظبوط، لسه صغيرون) بناءً على قيمته.
"""

def calculate_sum():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number + second_number

for attempt in range(3):
    total_result = calculate_sum()
    print(total_result)

    if total_result > 50:
        print("رقم تقيل")
    elif total_result > 20:
        print("مظبوط")
    else:
        print("لسه صغيرون")
