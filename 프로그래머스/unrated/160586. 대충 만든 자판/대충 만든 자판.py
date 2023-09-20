def solution(keymap, targets):
    answer = []
    for t in targets:
        a=0
        for i in t:
            b=1000000000000
            for k in keymap:
                if k.find(i)!=-1 and b>k.find(i):
                    b=k.find(i)+1
            if b==1000000000000: 
                a=-1
                break
            a+=b
        answer.append(a)
    return answer