def solution(k, tangerine):
    answer = 0
    td = [0] * 10000001
    
    for i in tangerine:
        td[i] += 1
    td.sort(reverse=True)
    # 1 2 2 1 2
    # 2 2 2 1 1
    idx = 0
    while idx < k :
        idx += td[answer]
        answer += 1
    
    return answer

# 개선책 1
# from collections import Counter

# def solution(k, tangerine):
#     answer = 0
#     # 귤 크기별 등장 횟수 카운팅
#     counts = Counter(tangerine)
    
#     # 등장 횟수만 내림차순 정렬 (최대 원소 수: tangerine 길이만큼만 정렬)
#     sorted_counts = sorted(counts.values(), reverse=True)
    
#     total = 0
#     for count in sorted_counts:
#         total += count
#         answer += 1
#         if total >= k:
#             break
            
#     return answer

# 개선책 2
# def solution(k, tangerine):
#     answer = 0
#     td = {}
    
#     for i in tangerine:
#         td[i] = td.get(i, 0) + 1
        
#     # 빈도수만 내림차순 정렬
#     counts = sorted(td.values(), reverse=True)
    
#     total = 0
#     for count in counts:
#         total += count
#         answer += 1
#         if total >= k:
#             break
            
#     return answer