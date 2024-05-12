def solution(s):
    answer = True

    l = list(s)
    temp=[]
    for i in range(len(l)):
        if temp[-1:] == []:
            temp.append(l[i])
        else:
            if temp[-1] != l[i] and l[i] == ")":
                temp.pop(len(temp)-1)
            else:
                temp.append(l[i])

    if len(temp)!=0:
        answer = False

    return answer