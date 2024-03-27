def whatayear(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False
year = int(input("Введите год: "))
if whatayear(year):
    print(f"{year} - високосный")
else:
    print("это год не високосный")