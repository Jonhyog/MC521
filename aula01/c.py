def solve(rounds):
    pt_count = {}

    # Finds high score m
    for (name, pt) in rounds:
        if name not in pt_count:
            pt_count[name] = 0
        pt_count[name] += pt
    m = max(pt_count.values())

    # Finds winner
    win_count = {}
    for (name, pt) in rounds:
        if name not in win_count:
            win_count[name] = 0
        win_count[name] += pt

        if win_count[name] >= m and pt_count[name] == m:
            return name

    return None

def main():
    n = int(input())
    parse = lambda t: (t[0], int(t[1]))

    rounds = []
    for _ in range(n):
        rounds.append(parse(input().split()))

    print(solve(rounds))

if __name__ == "__main__":
    main()