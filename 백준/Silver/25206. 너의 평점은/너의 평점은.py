ans=0
a=0
for _ in range(20):
  i=list(input().split())
  i[1]=float(i[1])
  if i[2]=='A+':
    ans+=i[1]*4.5
    a+=i[1]
  elif i[2]=='A0':
    ans+=i[1]*4.0
    a+=i[1]
  elif i[2]=='B+':
    ans+=i[1]*3.5
    a+=i[1]
  elif i[2]=='B0':
    ans+=i[1]*3.0
    a+=i[1]
  elif i[2]=='C+':
    ans+=i[1]*2.5
    a+=i[1]
  elif i[2]=='C0':
    ans+=i[1]*2.0
    a+=i[1]
  elif i[2]=='D+':
    ans+=i[1]*1.5
    a+=i[1]
  elif i[2]=='D0':
    ans+=i[1]*1.0
    a+=i[1]
  elif i[2]=='F':
    ans+=i[1]*0.0
    a+=i[1]
print(ans/a)