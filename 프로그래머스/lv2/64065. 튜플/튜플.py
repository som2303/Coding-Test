def solution(s):
    answer = []
    s=s[2:-2].split('},{')
    ans = []
    for i in s:
        i=i.split(',')
        ans.append(i)
    ans.sort(key=lambda x: len(x))
    for i in ans:
        for j in i:
            if int(j) not in answer: 
                answer.append(int(j))
                break

    return answer