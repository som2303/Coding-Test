def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]
    for i in numbers:
        if i in [1,4,7]: 
            answer+='L'
            left = [(i-1)//3, 0]
        elif i in [3,6,9]: 
            answer+='R'
            right = [(i-1)//3, 2]
        else:
            if i==0: i=10
            l = abs(left[0]-((i-1)//3))+abs(left[1]-1)
            r = abs(right[0]-((i-1)//3))+right[1]-1
            if l > r:
                answer+='R'
                right = [(i-1)//3, 1]
            elif l < r:
                answer+='L'
                left = [(i-1)//3, 1]
            else:
                if hand == "right": 
                    answer+='R'
                    right = [(i-1)//3, 1]
                else:
                    answer+='L'
                    left = [(i-1)//3, 1]
                    
    return answer