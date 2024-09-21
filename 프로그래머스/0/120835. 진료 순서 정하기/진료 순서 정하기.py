def solution(emergency):
    answer = []
    
    sortedEmergency = sorted(emergency, reverse = True)
    
    for i in emergency:
        idx = sortedEmergency.index(i)
        answer.append(idx + 1)
        
    return answer