"""
الوصف: برنامج فحص كلمة السر باستخدام While Loop،
يقوم بتسجيل وتخزين كل المحاولات الخاطئة في قائمة حتى إدخال رمز المرور الصحيح.
"""

CORRECT_PASSWORD = "1234"
failed_attempts = []

while True:
    user_input = input("ادخل كلمة السر: ")
    if user_input == CORRECT_PASSWORD:
        print("welcome")
        break
    else:
        print("try again")
        failed_attempts.append(user_input)

print("المحاولات الخاطئة التي تم تسجيلها:", failed_attempts)
