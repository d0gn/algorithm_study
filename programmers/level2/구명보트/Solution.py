def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    # 40 40 40 40 50 60 // 240
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            
        end -= 1
        answer += 1
            
    return answer