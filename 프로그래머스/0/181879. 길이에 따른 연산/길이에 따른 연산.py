def solution(num_list):
    a=0
    b=1
    for i in num_list:
        a+=i
        b*=i
    return a if len(num_list)>10 else b