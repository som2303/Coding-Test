from collections import deque
def fun(i,target):
    a=0
    for j in range(len(i)):
        if i[j]!=target[j]: a+=1
    if a>1:return False
    return True
def solution(begin, target, words):
    answer = 0
    t=[0 for i in range(len(words))]
    que=deque()
    que.append((begin,0))
    while que:
        a,b=que.popleft()
        if a==target: return b
        for i in range(len(words)):
            if fun(words[i],a) and t[i]==0:
                t[i]=b+1
                que.append((words[i],t[i]))
    return 0