n = str(input())
p = n.split(' ')
for i in p:
    i.split()
print(max(p, key=len))
l = 0
s = []
for r in p:
    if len(r) > l:
        s = [r]
        l = len(r)
    elif len(r) == l:
        s.append(r)
print(s)