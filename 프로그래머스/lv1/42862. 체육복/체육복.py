def solution(n, lost, reserve):
    stu=[1 for _ in range(n+1)]
    for i in lost: stu[i]=0
    for i in reserve:
        if stu[i]==0: stu[i]=1
        else: stu[i]=2
    for i in range(1,n+1):
        if stu[i]==2:
            if stu[i-1]==0:stu[i-1],stu[i]=1,1
            elif i!=n and stu[i+1]==0:stu[i+1],stu[i]=1,1
    
    return n-stu.count(0)