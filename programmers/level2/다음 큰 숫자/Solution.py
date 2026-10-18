def solution(n):
    answer = 0
    idx = bin(n)[2:].count('1')
    idx2 = 0
    i = 0
    while idx != idx2:
        i += 1
        idx2 = bin(n+i)[2:].count('1')
    print(idx)
    return n + i