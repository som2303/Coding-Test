def is_prime_num(n):
    n=int(n)
    if n==1: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True
def convert(n, k):
    num = '0123456789'
    if n//k==0: return str(n%k)
    return convert(n//k,k)+str(n%k)
def solution(n, k):
    answer = 0
    num=convert(n, k)
    now = ''
    for i in num:
        if i=='0': 
            if now and is_prime_num(now): answer+=1
            now=''
        else: now+=i
    if now and is_prime_num(now): answer+=1
    return answer