import sys
sys.setrecursionlimit(10000)

def solution(s):
    f=s[0]
    same=1
    diffent=0
    for i in range(1,len(s)-1):
        if f==s[i]:
            same+=1
        else:
            diffent+=1
        if same==diffent:
            return solution(s[i+1:])+1
    return 1