week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
chill_day = int(input("Сколько выходных на неделе вы хотите? "))
weekday = week[-chill_day:]
workday = week[:-chill_day]
print("Ваши выходные дни: ", "," .join(weekday))
print("Ваши рабочие дни: ", "," .join(workday))