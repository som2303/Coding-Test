l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
l3=list(map(int, input().split()))

def fun(l1,l2,l3):
  if l1[1]==l3[1]:
    y=l2[1]
    x=l3[0]
  else:
    y=l1[1]
    x=l3[0]
  return x,y
if l1[0]==l2[0]:

  x, y = fun(l1,l2,l3)
elif l3[0]==l2[0]:
  x, y = fun(l2,l3,l1)
else:
  x, y = fun(l3,l1,l2)
print(x,y)  