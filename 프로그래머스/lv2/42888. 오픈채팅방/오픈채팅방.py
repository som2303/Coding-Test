def solution(record):
    answer = []
    ans=[]
    name_id={}
    for i in record:
        a= i.split(' ')
        if a[0]=='Enter':
            ans.append([a[1],'들어왔습니다.'])
            name_id[a[1]]=a[2]
        elif a[0]=='Leave':
            ans.append([a[1],'나갔습니다.'])
        else: name_id[a[1]]=a[2]
    for i in ans:
        str1 = name_id[i[0]]+'님이 '+i[1]
        answer.append(str1)
    return answer