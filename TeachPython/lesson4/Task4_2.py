def s(n):
    ab, ac = 1,0
    b, c = 0,0
    lst = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        lst[b][c] = i
        na, nc = b + ab, c + ac
        if 0 <= na < n and 0 <= nc < n and not lst[na][nc]:
            b, c = na, nc
        else:
            ab, ac = -ac, ab
            b, c = b + ab, c + ac
    for b in list(zip(*lst)):
        print(*b)

s(int(input()))
