def solution(numbers):
    answer = []
    for num in numbers:
        if num%2==0: n=num+1
        else:
            b=bin(num)
            idx=b.rfind('0')
            if idx==0: n=int('0b10'+b[3:],2)
            else: 
                nb=b[:idx]+'10'
                if idx+2!=len(b):nb+=b[idx+2:]
                n=int(nb,2)
        answer.append(n)
    return answer