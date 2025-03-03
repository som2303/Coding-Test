a=[]
m=0
for _ in range(5):
    s=input()
    a.append(s)
    if m<len(s):
        m=len(s)
for i in range(m):
    for j in range(5):
        if i<len(a[j]):
            print(a[j][i], end='')