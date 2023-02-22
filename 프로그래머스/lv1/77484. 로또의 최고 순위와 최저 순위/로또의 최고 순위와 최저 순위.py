def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    for i in lottos:
        if i!=0:
            for j in win_nums:
                if i==j:
                    same+=1
                    break
        else: zero+=1
    answer = [min(7-same-zero,6),min(7-same,6)]
    return answer