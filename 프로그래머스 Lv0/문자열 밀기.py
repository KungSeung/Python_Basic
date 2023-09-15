def solution(A, B):
    answer = 0
    
    length = len(A)
    
    if A == B:
        return answer
        
    for i in range(0, length):
        moveChar = A[-1]
        newChar = moveChar + A[0:length-1]
        A = newChar
        answer += 1
        
        if(B == newChar):
            return answer
    
    if A != B:
        answer = -1
        return answer