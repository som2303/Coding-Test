def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    l=0
    r=len(people)-1
    while l<=r:
        answer+=1
        s=people[l]
        l+=1
        while s<limit and l<=r:
            if s+people[r]<=limit:
                r-=1
                s+=people[r]
            else: break
    return answer