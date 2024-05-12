import math, collections

def solution(progresses, speeds):
    answer = []
    temp = []
    
    for i in range(len(progresses)):
        k = math.ceil((100 - progresses[i])/speeds[i])
        if temp[-1:] != []:
            if temp[-1] > k:
                k = temp[-1]
        temp.append(k)
        
        
    return list(collections.Counter(temp).values())