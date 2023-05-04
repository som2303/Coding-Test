def solution(players, callings):
    pre_p = [i for i in range(-1,len(players)-1)]
    next_p = [i for i in range(1,len(players)+1)]
    head = 0
    dic = {i: num for num, i in enumerate(players)}
    for i in callings:
        call = dic[i]
        f_call = pre_p[call]
        b_call = next_p[call]
        ff_call = pre_p[f_call]

        if ff_call==-1:
            head=call
        pre_p[call]=ff_call
        if ff_call!=-1:
            next_p[ff_call]=call
        next_p[call]=f_call
        pre_p[f_call]=call
        next_p[f_call]=b_call
        if b_call<len(players):
            pre_p[b_call]=f_call
    
    answer = []
    while True:
        if head>len(players)-1:
            break
        answer.append(players[head])
        head = next_p[head]
    
    return answer