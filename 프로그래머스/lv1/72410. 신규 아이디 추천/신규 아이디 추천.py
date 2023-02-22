def solution(new_id):
    new_id = new_id.lower()
    ans = []
    answer = ''
    for i in new_id:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_.1234567890':
            ans.append(i)
    
    temp = ans[0]
    for i in ans:
        if i!='.' or (i=='.' and temp!=i):
            answer+=i
            temp =i
    if answer and answer[0]=='.': answer=answer[1:]
    if answer and answer[-1]=='.': answer=answer[:-1]
    
    if not answer: answer ='aaa'
    elif len(answer)>=16:
        if answer[14]=='.': answer = answer[:14]
        else: answer = answer[:15]
    while len(answer)<=2: answer+=answer[-1]
    return answer