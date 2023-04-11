def prime(n):
    if n<=1:return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return 0
    return 1
    
def fun(numbers,curr,ch,pr):
    for i in range(len(numbers)):
        n = curr+numbers[i]
        if not int(n) in ch:
            ch.append(int(n))
            if prime(int(n)): pr.append(int(n))
        a=numbers[:i]
        if i<len(numbers)-1: a+=numbers[i+1:]
        fun(a,n,ch,pr)

def solution(numbers):
    ch,pr=[],[]
    fun(numbers,'',ch,pr)
    return len(pr)