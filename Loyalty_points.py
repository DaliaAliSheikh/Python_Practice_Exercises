visits = [3, 5, 2, 8]

def calculate_points(visits):
    Total = 0
    for visit in visits:
        Total = Total + visit + 10
    return Total

print(calculate_points(visits), "وشكراً لزيارتك متجرنا")
