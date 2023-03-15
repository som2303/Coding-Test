def solution(N, stages):
    stage={i:[0,0] for i in range(1,N+1)}
    for i in stages:
        if i!=N+1:
            stage[i][0]+=1
            for j in range(1,i+1):
                stage[j][1]+=1
        else:
            for j in range(1,i):
                stage[j][1]+=1

    fail ={}
    for i,j in enumerate(stage.values()):
        if j[1]: fail[i+1]=j[0]/j[1]
        else: fail[i+1]=0
    fail=sorted(fail.items(), key= lambda x : x[1], reverse=True)
    answer = [i[0] for i in fail]
    
    return answer
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))