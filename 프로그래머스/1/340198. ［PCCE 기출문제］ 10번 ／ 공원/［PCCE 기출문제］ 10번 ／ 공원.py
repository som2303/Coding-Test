def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    
    dp = [[0 if i!='-1' else 1 for i in row] for row in park]
    
    for i in range(1, len(park)):
        for j in range(1, len(park[i])):
            if dp[i][j]!=0:
                dp[i][j]+=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                
    max_square_size = max(max(row) for row in dp)

    for mat in mats:
        if mat <= max_square_size:
            return mat
    
    return -1