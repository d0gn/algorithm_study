import math
def solution(arr):
    answer = 0
    temp = arr[0]
    for i in arr:
        temp = math.lcm(temp, i)
    return temp
