def solution(rny_string):
    answer = ''
    return ''.join([i if(i!='m') else 'rn' for i in rny_string ])