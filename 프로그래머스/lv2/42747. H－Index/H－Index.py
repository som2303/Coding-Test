def solution(citations):
    citations.sort(reverse=True)
    if citations==[0]:
        return 0
    for i in range(len(citations)):
        if citations[i]<=i:
            return i
    return len(citations)