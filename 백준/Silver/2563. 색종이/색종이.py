n= int(input())
ans=[]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
      for j in range(10):
        ans.append((a+i,b+j))

ans=set(ans)
print(len(ans))