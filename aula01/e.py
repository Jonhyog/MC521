def solve(students, n):
    gifts_count = {"1": 0, "2": 0, "3": 0}
    gifted_stds = {"1": [], "2": [], "3": []}

    # Counts categories occurences
    for idx, std in enumerate(students):
        gifts_count[std] += 1
        gifted_stds[std].append(idx + 1)
    
    # handles no teams case
    w = min(gifts_count.values())
    if w == 0:
        return 0, []
    
    # assigns teams
    teams = []
    for i in range(w):
        teams.append((
            gifted_stds["1"][i],
            gifted_stds["2"][i],
            gifted_stds["3"][i],
        ))
    
    return w, teams

def main():
    n = int(input())
    students = input().split()

    w, teams = solve(students, n)
    
    print(w)
    for i in range(w):
        print(" ".join(map(str, teams[i])))

if __name__ == "__main__":
    main()