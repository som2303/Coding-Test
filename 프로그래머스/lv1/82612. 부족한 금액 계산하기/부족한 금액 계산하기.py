def solution(price, money, count):
    return 0 if money>=(price*(count+1)*count/2) else (price*(count+1)*count/2) - money