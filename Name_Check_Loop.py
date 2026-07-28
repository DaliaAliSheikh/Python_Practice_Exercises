"""
الوصف: برنامج يطلب من المستخدم إدخال اسمه
ويكرر العملية 3 مرات للتفاعل مع المستخدم.
"""

for attempt in range(3):
    user_name = input("enter your name: ")
    if user_name == "مريم":
        print("اسم جميل")
    else:
        print("اسم رائع")
