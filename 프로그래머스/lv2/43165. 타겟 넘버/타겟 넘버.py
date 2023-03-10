def fun(now,idx,numbers):
    if idx>=len(numbers): 
        if now==0: return 1
        return 0
    if now>=numbers[idx]:
        return fun(now-numbers[idx],idx+1,numbers)+fun(now,idx+1,numbers)
    return fun(now,idx+1,numbers)
def solution(numbers, target):
    answer=0
    if sum(numbers)==target:return 1
    answer+=fun((sum(numbers)-target)//2,0,numbers)
    return answer