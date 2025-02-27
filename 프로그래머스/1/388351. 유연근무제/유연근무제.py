def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        a=1
        for j in range(len(timelogs[0])):
            t=(schedules[i]%100+10)%60+(schedules[i]%100+10)//60*100+schedules[i]//100*100
            if (startday+j)%7!=0 and (startday+j)%7!=6 and timelogs[i][j]>t:
                a=0
        if a:
            answer+=1
    return answer