def solution(n):
    answer = 0
    while True:
        if n<=7*answer:
            break
        answer+=1
    return answer