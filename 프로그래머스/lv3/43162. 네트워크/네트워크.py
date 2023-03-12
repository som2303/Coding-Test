from collections import deque
def fun(n,computers,idx):
    if not 1 in computers[idx]: return 0
    que=deque()
    que.append(idx)
    while que:
        b=que.popleft()
        for i in range(n):
            if computers[b][i]==1:
                computers[b][i],computers[i][b]=0,0
                if n!=i:que.append(i)
    return 1
def solution(n, computers):
    answer = 0
    for i in range(n):
        answer+=fun(n,computers,i)
    return answer