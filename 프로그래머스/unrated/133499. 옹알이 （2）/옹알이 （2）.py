def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    s = ''
    for i in babbling:
        e=1
        aa=''
        while e:
            print(1)
            e=0
            for j in a:
                if s+j == i[:len(s)+len(j)]:
                    if aa!=j:
                        s=s+j
                        e=1
                        aa=j
                        break
        
        if s==i:
            answer+=1
        s=''
    return answer