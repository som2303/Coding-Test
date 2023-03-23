def solution(s):
    d = {chr(ord('a')+i):0 for i in range(26)}
    for i in s:
        d[i]+=1
    answer = ''
    for i, j in d.items():
        if j==1:
            answer+=i
    return answer