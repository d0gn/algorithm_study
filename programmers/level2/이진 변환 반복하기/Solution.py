def solution(s):
    zero = 0
    count = 0
    while s != '1':
        zero += s.count('0')
        s = str(bin(s.count('1'))[2:])
        count += 1
        
    answer = [count, zero]
    return answer