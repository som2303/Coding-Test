def solution(wallpaper):
    a,b,c,d=len(wallpaper[0]),0,0,0
    e=0
    for j in range(len(wallpaper)):
        i=wallpaper[j]
        print(i.find('#'),i.rfind('#'))
        if a>i.find('#') and i.find('#')!=-1:
            a=i.find('#')
            if e==0:
                c=j
                e=1
        if b<i.rfind('#') and i.find('#')!=-1:
            b=i.rfind('#')
        if i.find('#')!=-1:
            d=j+1
    if b!=0 or d!=0: b+=1
    answer = [c,a,d,b]
    return answer