def solution(progresses, speeds):
    answer = []
    i=0
    n=-1
    tf=1
    while sum(progresses)<len(progresses)*100 and i<len(progresses):
        tf=1
        for j in range(i,len(progresses)):
            progresses[j]=min(100,progresses[j]+speeds[j])
            if tf==1 and progresses[j]==100: n=j
            else: tf=0
        
        if n>=i: 
            answer.append(n-i+1)
            i=n+1
        
    return answer