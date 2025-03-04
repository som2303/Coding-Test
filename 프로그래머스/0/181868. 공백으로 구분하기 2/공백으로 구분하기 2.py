def solution(my_string):
    answer=[]
    a=my_string.split(' ')
    for i in a:
        if i!='':
            answer.append(i)
    return answer