def solution(s):
    ans1,ans2=0,0
    while s!='1':
        ans1+=1
        s1=''
        for i in s:
            if i=='1':
                s1+='1'
            else:
                ans2+=1
        s=bin(len(s1))[2:]
    answer = [ans1,ans2]
    return answer