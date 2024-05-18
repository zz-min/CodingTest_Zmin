import heapq

# 풀이 3
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2: return -1
    
        s = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, s)
        answer += 1
        
        
    return answer

# 풀이 2
# def solution(scoville, K):
#     answer = 0 
    
#     while 1:        
#         s = min(scoville)
#         scoville.remove(min(scoville))
#         s += min(scoville) * 2
#         scoville.remove(min(scoville))
        
#         answer += 1
#         scoville.append(s)
        
#         if min(scoville) >= K : break    

#     return answer


# 풀이 1
# def solution(scoville, K):
#     answer = 0
    
#     while 1:     
#         scoville=sorted(scoville)
#         s = scoville[0] + scoville[1]*2
#         scoville.remove(scoville[1])
#         scoville.remove(scoville[0])
        
#         answer += 1
#         scoville.append(s)
        
#         if scoville[0] >= K : break    

#     return answer