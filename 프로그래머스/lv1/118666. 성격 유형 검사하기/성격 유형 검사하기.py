def solution(survey, choices):
    r = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    answer = ''
    for i in range(len(survey)):
        if choices[i]-4<0: r[survey[i][0]]+=4-choices[i]
        else:r[survey[i][1]]+=choices[i]-4
    if r['R']>=r['T']:answer+='R'
    else:answer+='T'
    if r['C']>=r['F']:answer+='C'
    else:answer+='F'
    if r['J']>=r['M']:answer+='J'
    else:answer+='M'
    if r['A']>=r['N']:answer+='A'
    else:answer+='N'
    return answer