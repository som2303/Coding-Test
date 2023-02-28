def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        j=0
        ans=0
        count = 1
        while True:
            if j+2*i-1<len(s):
                if s[j:j+i]==s[j+i:j+2*i]: count+=1
                else: 
                    if count ==1:ans+=i
                    else: 
                        ans=ans+i+len(str(count))
                        count=1
                        
            else:
                if count ==1:ans+=i
                else: 
                    ans=ans+i+len(str(count))
                    count=1
                break
            j+=i
        ans+=(len(s)%i)    
        if answer>ans: answer=ans
                
    return answer