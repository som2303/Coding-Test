def solution(cards1, cards2, goal):
    answer = 'Yes'
    i1, i2 = 0, 0
    for i in goal:
        if i1<len(cards1) and cards1[i1]==i:
            i1+=1
        elif i2<len(cards2) and cards2[i2]==i:
            i2+=1
        else:
            answer='No'
            break
    return answer