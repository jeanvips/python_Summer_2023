f0 = f1 = 1
n = int(input())
print(f0, f1, end=' ')
for i in range(2, n + 1):
    f0, f1 = f1, f0 + f1
    print(f1, end=' ')