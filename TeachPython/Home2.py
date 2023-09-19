x = int(input('Введите х: '))
y = int(input('Введите у: '))
if x+y > x-y:
    print(x+y)
elif x-y > x*y:
    print(x-y)
elif x*y > x/y:
    print(x*y)
elif x/y > x//y:
    print(x/y)
else:
    print(x//y)