def solution(price):
    answer = price
    if price>=100000:
        answer=price*0.95
    if price>=300000:
        answer=price*0.9
    if price>=500000:
        answer=price*0.8
    return answer//1