n = int(input())
dct = []
for i in range(1, n+1):
    if n % i == 0:
        dct.append(i)
print(dct)