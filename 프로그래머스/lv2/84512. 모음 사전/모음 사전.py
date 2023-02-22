def solution(word):
    words="AEIOU"
    answer = 0
    for i in range(len(word)):
        if words.index(word[i])>0:
            for j in range(1,6):
                c=words.index(word[i])            
                for l in range(j-i-1):
                    c*=5
                if j-i-1>=0:
                    answer+=c

    return answer+len(word)