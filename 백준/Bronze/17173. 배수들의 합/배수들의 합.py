l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
l=[0 for i in range(l1[0]+1)]
for i in l2:
  j=1
  while i*j<=l1[0]:
    l[i*j]=i*j
    j+=1
print(sum(l))