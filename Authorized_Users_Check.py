"""
الوصف: برنامج يفحص ما إذا كان الاسم المدخل ضمن قائمة المستخدمين المسموح لهم،
ويستمر في الطلب حتى إدخال اسم صحيح.
"""

allowed_users = ["ali", "ahmed", "omer"]

while True:
    user_name = input("ادخل اسمك: ")
    if user_name in allowed_users:
        print("ok")
        break
    else:
        print("حاول مرة أخرى")
