def solution(X, Y):
    answer = ''
    for i in range(9,-1,-1):
        x=X.count(str(i))
        y=Y.count(str(i))
        if answer=='' and i==0 and min(x, y)!=0:
            answer='0'
        else:
            answer+=str(i)*min(x,y)
    if answer=='':return '-1'
    return answer