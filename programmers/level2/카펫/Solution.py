def solution(brown, yellow):
    answer = []
    n = brown + yellow
    di = [i for i in range(1, n + 1) if n % i == 0]
    di.sort(reverse=True)
    print(di)
    for w in di:
        h = n // w
        if w < h:
            break
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
    
    return answer