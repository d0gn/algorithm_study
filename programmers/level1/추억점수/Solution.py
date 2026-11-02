def solution(name, yearning, photo):
    answer = []
    d = {}
    for i, j in zip(name, yearning):
        d[i] = j
        
    print(d)
    for p in photo:
        total = 0
        for o in p :
            if o in d:
                total += d[o]
        answer.append(total)
    return answer