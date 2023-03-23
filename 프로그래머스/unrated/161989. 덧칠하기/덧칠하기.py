def solution(n, m, section):
    answer = 0
    now=section[0]
    for i in section:
        if now<=i:
            answer+=1
            now=i+m
    return answer