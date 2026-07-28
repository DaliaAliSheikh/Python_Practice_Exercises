"""
الوصف: برنامج يطلب من المستخدم إدخال رقمين ويجمعهما، 
ويكرر هذه العملية 3 مرات باستخدام الحلقة التكرارية،
مع فحص ما إذا كان الناتج يساوي 30 في كل مرة.
"""

def check_sum():
    first_number = float(input("enter the first number: "))
    second_number = float(input("enter the second number: "))
    return first_number + second_number

for i in range(3):
    result = check_sum()
    print("the result is", result)
    
    if result == 30:
        print("ok")
    else:
        print("ol")
