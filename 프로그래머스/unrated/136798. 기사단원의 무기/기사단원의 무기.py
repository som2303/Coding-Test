def solution(number, limit, power):
    p=[2 for i in range(number)]
    p[0]=1
    for i in range(2,number+1):
        if (i**0.5)%1==0:
            p[i-1]+=1
            for j in range(2,int(i**0.5)):
                if i%j==0:
                    p[i-1]+=2
        else:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    p[i-1]+=2
        
        if p[i-1]>limit:
            p[i-1]=power
    return sum(p)