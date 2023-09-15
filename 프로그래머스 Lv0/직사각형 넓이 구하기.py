def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    print(x)
    print(y)
    w = max(x) - min(x)
    h = max(y) - min(y)
    area = w*h
    return area

# w = max(dots)[0] - min(dots)[0]
# h = max(dots)[1] - min(dots)[1]