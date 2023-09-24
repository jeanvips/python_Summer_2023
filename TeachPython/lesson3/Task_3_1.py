lst = []
zp = 0
while True:
    n = int(input())
    if n == 0: break
    lst.append(n)
    zp += n
a = len(lst)
print(zp/ a)

