a = list(map(int, input().split()))
ans=-1
for i in range(6):
  if a.count(i+1)==3:
    ans=10000+(i+1)*1000
    print(ans)
    break
  if a.count(i+1)==2:
    ans=1000+(i+1)*100
    print(ans)
    break
if ans==-1:
    print(max(a)*100)