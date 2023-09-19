x = int(input('Введите х: '))
y = int(input('Введите у: '))
a = x + y
b = x - y
c = x*y
d = x/y
e = x//y
ads = [a,b,c,d,e] #задаю список
asb = set(ads) #оставляю уникальные числа
asb.remove(max(asb))#убираю максимальное
print(max(asb))