import math

def solution(n, m):
    answer = []
    gcd = math.gcd(n, m)
    lcm = math.lcm(n, m)
    return [gcd, lcm]