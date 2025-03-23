while True:
  a=int(input())
  if a==-1:
    break
  p=[]
  for i in range(1,int(a**(1/2))+1):
    if a%i==0:
      p.append(i)
      if a//i!=i and a//i!=a:
        p.append(a//i)
  p.sort()
  if sum(p)==a:
    s=' + '.join([str(i) for i in p])
    print(f"{a} = {s}")
  else:
    print(f"{a} is NOT perfect.")