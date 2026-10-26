def solution(elements):
    answer = 0
    # 7 9 1 1 4
    # temp.append(sum(elements[i:i+j]))
    # 시작값 i = 0 ~ 길이 j 는 끝값
    temp = []
    el = len(elements)
    extended = elements * 2
    
    for i in range(el): # 0 ~ 4
        for j in range(el): # 0 ~ 4
            temp.append(sum(extended[j:j+i]))
        
    answer = len(list(set(temp)))
        
    return answer