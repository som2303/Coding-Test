def fun(skill, skill_tree):
    n1=0
    n2=0
    while n1<len(skill)-1 and n2<len(skill_tree):
        a=skill_tree[n2]
        # print(a,que,skill_tree)
        if skill[n1]==a:n1+=1
        elif a in skill[n1+1:]: return 0
        n2+=1
    return 1
    

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer+=fun(skill, skill_tree)
        print(answer)
    return answer