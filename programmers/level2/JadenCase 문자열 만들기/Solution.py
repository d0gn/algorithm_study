def solution(s):
    ls = s.split(' ')
    for i in range(len(ls)):
        ls[i] = ls[i].capitalize()
    return ' '.join(ls)