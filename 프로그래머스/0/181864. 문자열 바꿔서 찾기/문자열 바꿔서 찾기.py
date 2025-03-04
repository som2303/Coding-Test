def solution(myString, pat):
    return 1 if pat in myString.replace('A','b').replace('B','a').upper() else 0