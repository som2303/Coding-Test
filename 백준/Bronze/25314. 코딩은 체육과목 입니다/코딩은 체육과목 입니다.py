n = int(input())
for i in range(n//4):
    print("long", end = ' ')
if n%4!=0:
    print("long", end = ' ')
print("int")