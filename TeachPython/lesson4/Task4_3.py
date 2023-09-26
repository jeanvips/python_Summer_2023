def a(lst):
    s = {}
    for i in lst.lower():
        if i.isalpha():
            s[i] = s.get(i,0) + 1
    return s
print('True' if a(input()) == a(input()) else 'False')