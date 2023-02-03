def solution(today, terms, privacies):
    answer = []
    t = {}
    for i in terms:
        t[i[0]]=int(i[2:])
        
    ty, tm, td= map(int, today.split("."))
    for i in range(len(privacies)):
        day, term=privacies[i].split()
        y,m,d = map(int, day.split("."))
        add = t[term]
        y += add//12
        m += add%12
        if m > 12:
            y += 1
            m -= 12
        
        if y < ty:
            answer.append(i+1)
        elif y == ty:
            if m < tm:
                answer.append(i+1)
            elif m == tm and d <= td:
                answer.append(i+1)
    return answer