def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 10 + 1):
        dic = dict()
        for o, k in zip(want, number):
            dic[o] = k
            
        for j in range(i, i + 10):
            item = discount[j]
            if item in dic and dic[item] > 0:
                dic[item] -= 1
            else :
                break
        else:
            answer += 1               
        
    return answer