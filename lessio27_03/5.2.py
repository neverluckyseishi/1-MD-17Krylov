import random
numb = [random.randint(1, 10) for _ in range(10)]
i = set()
for num in numb:
    if numb.count(num) > 1:
        i.add(num)
if i:
    print("Повторяющиеся элементы:", i)
else:
    print("Повторяющихся элементов нет.")
print("Исходный список:", numb)