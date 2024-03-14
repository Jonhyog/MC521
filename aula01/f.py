def solve(lanterns, n, l):
    max_diff = 0

    for i in range(0, n - 1):
        max_diff = max(max_diff, lanterns[i + 1] - lanterns[i])
    
    first_l = lanterns[0]
    last_l = lanterns[-1]

    possible = [first_l, max_diff / 2, l - last_l]

    return max(filter(lambda x: x != 0, possible))

def main():
    n, l = map(int, input().split())
    lanterns = sorted(map(int, input().split()))

    print(f"{solve(lanterns, n, l):.10f}")

if __name__ == "__main__":
    main()