s = int(input())
i = [0] * 10
while s > 0:
    a = s % 10
    i[a] += 1
    s = s // 10
r = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for w in range(10):
    print(r[w], '-', i[w])
