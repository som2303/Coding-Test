def solution(video_len, pos, op_start, op_end, commands):
    start=int(op_start[:2])*60+int(op_start[3:])
    end=int(op_end[:2])*60+int(op_end[3:])
    n=int(pos[:2])*60+int(pos[3:])
    total=int(video_len[:2])*60+int(video_len[3:])
    for c in commands:
        if n<=end and n>=start:
            n=end
        if c=='prev':
            n-=10
            if n<0:
                n=0
        else:
            n+=10
            if n>total:
                n=total
    if n<=end and n>=start:
        n=end
    m=n//60
    s=n%60
    answer = f'{m:0>2}:{s:0>2}'
    return answer