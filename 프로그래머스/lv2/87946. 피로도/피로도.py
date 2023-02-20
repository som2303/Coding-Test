def solution(k, dungeons):
    ans = [0]
    def fun(k1, dungeons1,cnt):
        for i in range(len(dungeons1)):
            if dungeons1[i][0]<=k1:
                a=dungeons1[:i]
                if i<len(dungeons1)-1:a+=dungeons1[i+1:]
                fun(k1-dungeons1[i][1],a,cnt+1)
        ans.append(cnt)
    
    fun(k, dungeons,0)
    return max(ans)