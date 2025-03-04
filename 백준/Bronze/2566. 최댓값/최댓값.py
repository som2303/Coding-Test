M=-1
Mix=-1
Miy=-1
for i in range(9):
    a=list(map(int,input().split()))
    for j in range(9):
      if M<a[j]:
        M=a[j]
        Mix=i
        Miy=j
print(M)
print(Mix+1, Miy+1)