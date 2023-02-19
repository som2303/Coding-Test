def solution(food):
    answer = ''
    n=1
    for i in food[1:]:
        answer+=str(n)*(i//2)
        n+=1
    return answer+'0'+answer[::-1]