import numpy as np
def solution(id_list, report, k):
    id_dic = {i:j for j, i in enumerate(id_list)}
    r=set(report)
    size = len(id_list)
    count = np.array([[0 for i in range(size)]]*size)
    
    for i in r:
        l=i.split(" ")
        count[id_dic[l[0]]][id_dic[l[1]]]=1
    c=np.sum(count, axis=0)
    answer = [0 for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if c[i]>=k and count[j][i]:
                answer[j]+=1
    
    return answer