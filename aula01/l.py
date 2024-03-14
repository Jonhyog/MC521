def solve(numbers, n):
    first_3_sum = (numbers[0] % 2) + (numbers[1] % 2) + (numbers[2] % 2)
    evenness = 0 if first_3_sum < 2 else 1
    
    for i in range(n):
        if numbers[i] % 2 != evenness: return i + 1
    
    return -1

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    print(solve(numbers, n))

if __name__ == "__main__":
    main()