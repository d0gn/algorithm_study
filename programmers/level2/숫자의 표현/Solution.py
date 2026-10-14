def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
    return answer
    # return len([i for i in range(1, n + 1, 2) if n % i == 0]) 이 경우가 정수의 성질을 이용한 풀이 방법