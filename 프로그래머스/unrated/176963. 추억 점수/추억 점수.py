def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    print(dic)
    answer = []
    for i in photo:
        ans=0
        for j in i:
            if j in name:
                ans+=dic[j]
        answer.append(ans)
        
    return answer