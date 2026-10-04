def solution(s):
    answer = False
    c = 0
    for i in s:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        
        if c < 0:
            return False
    
    if c == 0 :
        answer = True

    return answer