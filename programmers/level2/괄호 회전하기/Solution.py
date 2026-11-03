def iv(s):
    stack = []
    pair = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in pair.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    if len(s) % 2 != 0:
        return 0
    n = len(s)
    answer = 0
    for x in range(n):
        rotated = s[x:] + s[:x]
        if iv(rotated):
            answer += 1

    return answer