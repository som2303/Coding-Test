def solution(k, score):
    answer = []
    m=[]
    for i in range(len(score)):
        if i<k: 
            m.append(score[i])
            m.sort()
            
        else:
            if m[0]< score[i]:
                m[0]=score[i]
                m.sort()
        answer.append(m[0])
            
    return answer