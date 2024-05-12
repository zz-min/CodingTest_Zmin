def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(completion.__len__()):
        if participant[i] != completion[i]:
            return participant[i]
                       
    return participant[completion.__len__()]