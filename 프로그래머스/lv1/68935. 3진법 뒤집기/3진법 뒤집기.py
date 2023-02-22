def solution(n):
    a=''
    answer = 0
    while n>0:
        a+=str(n%3)
        n=n//3
    for i in range(len(a)):
        answer+=int(a[i])*3**(len(a)-i-1)
    
    return answer