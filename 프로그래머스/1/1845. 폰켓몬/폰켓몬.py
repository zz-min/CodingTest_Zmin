from collections import Counter

def solution(nums):
    a=nums.__len__()/2 #선택할 수 있는 개수
    
    counter = Counter(nums)
    b=dict(counter).keys().__len__() #종류 개수
    
    if a>b:
        answer = b
    else:
        answer = a
        
    return answer