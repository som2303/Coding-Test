def solution(data, ext, val_ext, sort_by):   
    answer = []
    vals=["code", "date", "maximum", "remain"]
    for i in data:
        for j in range(4):
            if ext==vals[j] and i[j]<val_ext:
                answer.append(i)
                break
    for j in range(4):
        if sort_by==vals[j]:
            answer.sort(key= lambda x:x[j])
    return answer