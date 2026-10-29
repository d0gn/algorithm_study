def solution(n,a,b):
    answer = 0
    while n != 1:
        if (a+1) // 2 == (b+1) // 2:
            break
        n = n // 2
        a, b = (a+1) // 2, (b + 1) // 2        
        answer += 1
    return answer + 1