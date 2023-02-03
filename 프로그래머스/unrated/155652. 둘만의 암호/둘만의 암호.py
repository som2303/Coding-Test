def solution(s, skip, index):
    a_z = [chr(i) for i in range(97,123)]
    for i in skip:
        a_z.remove(i)
    answer = ''
    for i in s:
        idx = (a_z.index(i)+index)%len(a_z)
        answer+=a_z[idx]
    return answer