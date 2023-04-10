def solution(answers):
    answer=[]
    a=[1,2,3,4,5]; b=[2,1,2,3,2,4,2,5]; c=[3,3,1,1,2,2,4,4,5,5]
    aa=0; bb=0; cc=0 #인덱스 번호
    aaa=0; bbb=0; ccc=0 #맞춘 개수
    for i in range(len(answers)):
        if answers[i]==a[aa]:
            aaa+=1
        if answers[i]==b[bb]:
            bbb+=1
        if answers[i]==c[cc]:
            ccc+=1
        aa+=1; bb+=1; cc+=1
        if aa==5:
            aa=0
        if bb==8:
            bb=0
        if cc==10:
            cc=0
    s=max([aaa,bbb,ccc])
    if s==aaa:
        answer.append(1)
    if s==bbb:
        answer.append(2)
    if s==ccc:
        answer.append(3)
    return answer