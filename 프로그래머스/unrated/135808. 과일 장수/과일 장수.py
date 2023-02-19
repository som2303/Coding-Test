def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        if m+i-1<len(score):
            answer+=m*score[m+i-1]
    return answer