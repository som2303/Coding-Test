a=[i+1 for i in range(30)]
for _ in range(28):
    a.remove(int(input()))

print(a[0])
print(a[1])