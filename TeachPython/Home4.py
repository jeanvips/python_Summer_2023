a = int(input())
for q in range(1, 10):
    if q > 9:  # Ограничитель, числа после 9 не выводятся
        break
    print(q * a)