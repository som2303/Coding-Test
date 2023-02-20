def cal(fees,time):
    if (time-fees[0])%fees[2]: a= (time-fees[0])//fees[2]+1
    else: a= (time-fees[0])//fees[2]
    return fees[1]+a*fees[3]
def solution(fees, records):
    records.sort(key= lambda x:x[6:10])
    now=records[0][6:10]
    time=records[0][:5]
    all_time = 0
    answer = []
    for i in records[1:]:
        if now==i[6:10]:
            if i[-1]=='N': time=i[:5]
            elif i[-1]=='T' and time:
                all_time+=int(i[:2])*60+int(i[3:5])-int(time[:2])*60-int(time[3:])
                time=''
        else:
            if time: 
                all_time+=1439-int(time[:2])*60-int(time[3:])
                time=''
            if all_time<=fees[0]: answer.append(fees[1])
            else: answer.append(cal(fees,all_time))
            all_time=0
            time=i[:5]
            now=i[6:10]
    if time: 
        all_time+=1439-int(time[:2])*60-int(time[3:])
        time=''
    if all_time<=fees[0]: answer.append(fees[1])
    else: answer.append(cal(fees,all_time))
    return answer