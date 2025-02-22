n, m =map(int, input().split())
a=[i+1 for i in range(n)]
for _ in range(m):
    f,s =map(int, input().split())
    fa=a[f-1]
    a[f-1]=a[s-1]
    a[s-1]=fa
for i in range(n):
    print(a[i],end=' ')