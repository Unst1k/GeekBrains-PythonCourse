seconds = int(input('Введите время в секундах: '))

hours = seconds // (60*60)
seconds %= (60*60)
minutes = seconds // 60
seconds %= 60

print("%02i:%02i:%02i" % (hours, minutes, seconds))
