result = " "
while True:
    word = input("Введите слово ")
    if word.lower() == "stop":
        break
    result += word + " "
print("Итоговая строка :", result.strip())
