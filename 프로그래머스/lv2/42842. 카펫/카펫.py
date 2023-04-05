def solution(brown, yellow):
    answer = []
    for c in range(3,int((brown+yellow)**(1/2))+1):
        if (brown+yellow)%c==0:
            r=(brown+yellow)/c
            for j in range(1,c):
                if yellow == (r-2*j)*(c-2*j):
                    answer=[r,c]         
    return answer