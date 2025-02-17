def solution(board, h, w):
    answer = 0
    now=board[h][w]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in direction:
        nh=h+i[0]
        nw=w+i[1]
        if nh>=0 and nh<len(board) and nw>=0 and nw<len(board[0]):
            if now==board[nh][nw]:
                answer+=1
    return answer