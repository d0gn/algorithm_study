def solution(n):
    answer = 0
    Tb = 3
        # 1 3 9 27 81 이런식으로 계속 커진다. 그럼 45는 81 보다 작으므로 27 에서 몫을 나누면
        # 1이 나오고 나머지는 18 이후 27 아래 정수인 9에서 몫을 구하면 2로 나누어 떨어짐
        # 나머지 값들은 0, 0 으로 종료
    while n >= Tb:
        Tb *= 3
    print(Tb // 3)
    ttb = Tb // 3
    TBS = ''
    while ttb != 0:
        TBS += str(n // ttb)
        n = n % ttb
        ttb = ttb // 3
    
    print(TBS)
    
    RTBS = TBS[::-1]
    print(RTBS)
    
    RTBSL = len(RTBS)
    print(3**0)
    
    for i in range(0, len(RTBS)):
        answer += int(RTBS[i]) * (3**(RTBSL-(i + 1)))
    return answer



# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3)
#     return answer