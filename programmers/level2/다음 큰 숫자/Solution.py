def solution(s):
    answer = ''
    l = [int(i) for i in s.split(' ')]
    answer = str(min(l)) + ' ' + str(max(l))
    return answer