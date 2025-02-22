n, m = map(int, input().split())
a=[i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j-i+1)//2):
        p=a[i+k-1]
        a[i+k-1]=a[j-k-1]
        a[j-k-1]=p

for i in range(n):
    print(a[i], end=' ')