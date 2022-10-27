file = open("numbers.txt", "r")

for string in file:
    t = string.replace("\n", "")
    print ( f"Квадрат числа {t} равен {float(t)**2}")




