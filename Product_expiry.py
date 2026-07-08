days_left = [10, -2, 5, 0, -1]

def check_expiry(days_left):
    for day in days_left:
        if day <= 0:
            print(day, "expired product")
        else:
            print(day, "product is safe")

check_expiry(days_left)
