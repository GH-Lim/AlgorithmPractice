# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C, D):
    # write your code in Python 3.6
    digit = [A, B, C, D]
    visited = set()
    for a in range(4):
        if digit[a] > 2: continue
        for b in range(4):
            if b == a: continue
            if digit[a] == 2 and digit[b] >= 4: continue
            for c in range(4):
                if c == a or c == b: continue
                if digit[c] > 5: continue
                for d in range(4):
                    if d == a or d == b or d == c: continue
                    if digit[d] > 9: continue
                    visited.add((digit[a], digit[b], digit[c], digit[d]))
    return len(visited)
