def solution(name):
    if name=='A'*len(name):
        return 0
    answer = 0
    a=[len(name)-1]
    a1,a2=-1,0
    b=''
    for i in range(len(name)):
        b+='A'
        answer+=min(ord(name[i])-ord('A'),ord('Z')-ord(name[i])+1)
        if name[i]=='A':
            if a1==-1:
                a1=i
            a2+=1
        else:
            if a1==0:
                a.append(len(name)-a2)
            # elif a1+a2+1==len(name):
            #     print(1)
            #     a.append(a2)
            elif a1!=-1:
                a.append(min(len(name)-a2+a1-2,2*len(name)-a1-2*a2-1))
            a1,a2=-1,0
        if a1+a2==len(name):
            a.append(a1-1)
    answer+=min(a)
    
    return answer