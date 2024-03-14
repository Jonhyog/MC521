def solve(a, b):
    if a == b:
        return 0
    
    return 1 if a > b else -1

def main():
    a = str(input()).lower()
    b = str(input()).lower()

    print(solve(a, b))

if __name__ == "__main__":
    main()