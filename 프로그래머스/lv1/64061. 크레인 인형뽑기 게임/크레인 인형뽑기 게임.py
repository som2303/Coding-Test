def solution(board, moves):
    answer = 0
    basket = []
    size = len(board)
    for m in moves:
        for i in range(size):
            if board[i][m-1]:
                if not basket: basket.append(board[i][m-1])
                else:
                    if basket[-1]==board[i][m-1]:
                        basket.pop()
                        answer+=2
                    else: basket.append(board[i][m-1])
                board[i][m-1]=0
                break
    return answer