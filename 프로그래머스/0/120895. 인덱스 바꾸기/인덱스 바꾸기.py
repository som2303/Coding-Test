def solution(my_string, num1, num2):
    m=min(num1, num2)
    M=max(num1, num2)
    return my_string[:m]+my_string[M]+my_string[m+1:M]+my_string[m]+my_string[M+1:]