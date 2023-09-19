x = int(input('Введите х: '))
y = int(input('Введите у: '))
a = x + y
b = x - y
c = x*y
d = x/y
e = x//y
ads = [a,b,c,d,e]
res = set(ads)
res.remove(max(res))
print(max(res))