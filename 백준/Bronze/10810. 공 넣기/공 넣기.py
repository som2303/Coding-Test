n,m= map(int, input().split())
a=[0]*n
for _ in range(m):
    i, j, k = map(int, input().split()) 
    for l in range(i-1, j):
        a[l]=k
for i in range(n):
    print(a[i],end=' ')