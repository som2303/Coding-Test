def solution(a, b):
    while b%2==0:
        b=b/2
    while b%5==0:
        b=b/5
    if b!=1 and a%b!=0:
        return 2
    return 1