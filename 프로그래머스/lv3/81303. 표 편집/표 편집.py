def solution(n, k, cmd):
    res = ''
    pre =[]
    next =[]
    ft =[True]*n
    exist = []
    for i in range(n):
        pre.append(i-1)
        next.append(i+1)
    next[-1]=-1
    now = k
    for i in cmd:
        if (i[0]=='U'):
            j=int(i[2:])
            while j>0:
                if pre[now]!=-1:
                    j-=1
                    now=pre[now]
                else: break
        elif(i[0]=='D'):
            j=int(i[2:])
            while j>0:
                if next[now]!=-1:
                    j-=1
                    now=next[now]
                else: break
        elif(i[0]=='C'):
            exist.append(now)
            ft[now]=False
            if pre[now]==-1: 
                pre[next[now]]=pre[now]
                now = next[now]
            
            elif next[now]==-1: 
                next[pre[now]]=next[now]
                now = pre[now]
            else:  
                next[pre[now]]=next[now]
                pre[next[now]]=pre[now]
                now = next[now]

        else:
            p=exist.pop()
            ft[p]=True
            if pre[p]==-1:
                pre[next[p]]=p
            elif next[p]==-1:
                next[pre[p]]=p
            else:
                pre[next[p]]=p
                next[pre[p]]=p

    for i in ft:
        if i:
            res+="O"
        else:
            res+="X"

    return res