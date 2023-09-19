x = int(input())
y = int(input())
a = x + y
b = x - y
c = x*y
d = x/y
e = x//y
if a > b and a > c and a > d and a > e:
    print(a)
elif b > c and b > d and b > e:
    print(b)
elif c > d and c > e:
    print(c)
elif d > e:
    print(d)
else:
    print(e)