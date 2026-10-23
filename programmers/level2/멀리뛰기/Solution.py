def solution(n):
    if n <= 2:
        return n
    n1, n2 = 1, 2
    
    for i in range(3, n+1):
        n1, n2 = n2, (n1+n2) % 1234567
    
    return n2