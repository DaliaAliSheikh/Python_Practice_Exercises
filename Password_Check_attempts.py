"""
الوصف: برنامج فحص كلمة السر يمنح المستخدم 3 محاولات،
وفي حال الفشل في كافة المحاولات يتم تقييد الحساب باستخدام تركيب for-else.
"""

CORRECT_PASSWORD = "دلويه123"

for attempt in range(1, 4):
    user_input = input("ادخل كلمة السر: ")
    if user_input == CORRECT_PASSWORD:
        print("مرحب بيك يا مديرة")
        break
    else:
        print("غلط حاول تاني")
else:
    print("حسابك اتقفل")
