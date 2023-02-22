def distance(i,j,k):                            
    if i+1<=4:
        if k[i+1][j]=='P': return 0
    if i+2<=4:
        if k[i+2][j]=='P' and k[i+1][j]=='O': return 0
    if i+1<=4 and j-1>=0: 
        if k[i+1][j-1]=='P' and (k[i][j-1]=='O' or  k[i+1][j]=='O'): return 0
    if j+1<=4:
        if k[i][j+1]=='P': return 0
    if j+2<=4:
        if k[i][j+2]=='P' and k[i][j+1]=='O': return 0
    if i+1<=4 and j+1<=4: 
        if k[i+1][j+1]=='P' and (k[i][j+1]=='O' or  k[i+1][j]=='O'): return 0
    return 1
                

def solution(places):
    p1=[]
    answer = []
    for j in places:
        p=[]
        for i in j:
            p.append([i[0],i[1],i[2],i[3],i[4]])
        p1.append(p)
    
    for k in p1:
        ans=1
        for i in range(5):
            if ans==0: break
            for j in range(5):
                if ans==0: break
                if k[i][j]=='P': ans=distance(i,j,k)
                
        answer.append(ans)     
    
    return answer