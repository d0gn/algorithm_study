def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1 = 0
    c2 = 0
    for i in goal:
        if len(cards1) > c1 and cards1[c1] == i:
            c1 += 1
            continue
        elif len(cards2) > c2 and cards2[c2] == i:
            c2 += 1
            continue
        else :
            answer = "No"
    return answer