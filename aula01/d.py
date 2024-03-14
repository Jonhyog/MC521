def solve(n, m, a, b):
    eq_pta, eq_ptb = m * a, b

    if eq_ptb > eq_pta:
        return n * a
    
    return (n // m) * b + min((n % m) * a, b)

def main():
    n, m, a, b = map(int, input().split())

    print(solve(n, m, a, b))

if __name__ == "__main__":
    main()