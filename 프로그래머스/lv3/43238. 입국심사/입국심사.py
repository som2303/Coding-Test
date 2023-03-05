def solution(n, times):
    times.sort()
    answer = 1e18
    left,right=0,1e18
    while left<=right:
        mid=(left+right)//2
        s=0
        for i in times:
            s+=mid//i
            if s>=n: 
                right=mid-1
                answer=mid
                break
        if s<n:left=mid+1
    return answer