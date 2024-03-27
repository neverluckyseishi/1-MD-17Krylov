import random
we = ["Крылов", "Максаков", "Опарин", "Платонов", "Резницкий", "Воронов", "Зданевич", "Сосов", "Фалко"]
other = ["Иванов", "Светлов", "Петров", "Носов", "Летов", "Правов", "Левов", "Краснов", "Судов", "Фролов", "Маликов"]
team = tuple(random.sample(we, 6) + random.sample(other, 6))
print("Группа 1:", we)
print("Группа 2:", other)
print("Комманда:", team)
print("Длинна кортежа:", len(team))
high_team = tuple(sorted(team))
print("Отсортированная команда:", high_team)
if "Иванов" in team:
    n = team.count("Иванов")
    print("Студент входит в команду", n, "раз")
else:
    print("Студент не входит в команду")