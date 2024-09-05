seconds = int(input('введите число от 0 до 8640000'))
day, seconds = divmod(seconds, 86400)
hour, seconds = divmod(seconds,3600)
minutes, seconds = divmod(seconds, 60)


days = ['день', 'дней', 'дня']
quantity = []
if day == 11:
    quantity = days[1]
elif day % 10 == 1:
    quantity = days[0]
elif day % 10 > 1 and day % 10 <= 4:
    quantity = days[2]

else:
    quantity = days[1]



print( f'{day} {quantity}, {hour:02}:{minutes:02}:{seconds:02}')
