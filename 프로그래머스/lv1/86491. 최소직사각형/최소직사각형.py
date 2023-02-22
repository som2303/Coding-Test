def solution(sizes):
    r,h=0,0
    for i in sizes:
        r1,h1=max(i),min(i)
        if r1>r:r=r1
        if h1>h:h=h1
    return r*h