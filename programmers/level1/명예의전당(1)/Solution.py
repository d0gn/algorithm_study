import heapq
def solution(k, score):
    answer = []
    minh = []
    for s in score:
        heapq.heappush(minh, s)
        if len(minh) > k:
            heapq.heappop(minh)
        print(minh)
        answer.append(minh[0])
        
    return answer