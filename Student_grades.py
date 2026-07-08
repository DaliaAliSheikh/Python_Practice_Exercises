grades = [85, 90, 75, 95]

def calculate_total_grades(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return total

print(calculate_total_grades(grades), "هو مجموع درجاتك")
