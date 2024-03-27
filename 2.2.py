seat_number = int(input("Введите номер места: "))
def whatatype(seat_number):
    if seat_number % 2 == 0:
        seat_type = "нижнее"
    else:
        seat_type = "верхнее"
    if seat_number % 4 == 1 or seat_number % 4 == 2:
        seat_type += " боковое"
    else:
        seat_type += " купе"
    return seat_type
result = whatatype(seat_number)
print("Тип места: " + result)