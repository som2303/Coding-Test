def fun(s,idx):
    l=[]
    l1='[{('
    l2=']})'
    for i in range(len(s)):
        n=(idx+i)%len(s)
        if l==[] and s[n] in l2: return 0
        elif s[n] in l1: l.append(s[n])
        elif l2.find(s[n])==l1.find(l[-1]):l.pop()
        else: return 0
    return 1
    
def solution(s):
    if len(s)%2==1: 
        return 0
    if fun(s,0)==1: return len(s)/2
    answer = 0
    for i in range(1,len(s)):
        answer+=fun(s,i)
    return answer