def solution(park, routes):
    start = [0, 0]
    h, w = len(park),len(park[0]) 
    for i in range(h):
        for j in range(w):
            if park[i][j]=='S':
                start=[i,j]
                break
                
    for i in routes:
        a=0
        if i[0]=='N':
            if start[0]-int(i[2:])>=0:
                for j in range(int(i[2:])+1):
                    if park[start[0]-j][start[1]]=='X':
                        a=1
                        break
                if a==0:
                    start[0]-=int(i[2:])
        elif i[0]=='S':
            if start[0]+int(i[2:])<h:
                for j in range(int(i[2:])+1):
                    if park[start[0]+j][start[1]]=='X':
                        a=1
                        break
                if a==0:
                    start[0]+=int(i[2:])
        elif i[0]=='W':
            if start[1]-int(i[2:])>=0:
                for j in range(int(i[2:])+1):
                    if park[start[0]][start[1]-j]=='X':
                        a=1
                        break
                if a==0:
                    start[1]-=int(i[2:])
            
        elif i[0]=='E':
            if start[1]+int(i[2:])<w:
                for j in range(int(i[2:])+1):
                    if park[start[0]][start[1]+j]=='X':
                        a=1
                        break
                if a==0:
                    start[1]+=int(i[2:])         
    return start