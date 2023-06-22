def solution(s):
    answer = []
    for i in range(len(s)):
        if s[:i].rfind(s[i])==-1:
            answer.append(s[:i].rfind(s[i]))
        else:
            answer.append(i-s[:i].rfind(s[i]))
    return answer