# def solution(arr):
#     answer = [arr[0]]
    
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i+1])
        
#     return answer

def solution(arr):
    answer = []
    
    for i in arr:
        if answer[-1:] == [i]: 
            continue
        answer.append(i)
        
    return answer

