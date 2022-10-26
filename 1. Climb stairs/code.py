def solve(n):
    # 1. Base cases
    if n == 0: return 1
    if n < 0: return 0
    
    # 2. Normal cases
    return solve(n-1) + solve(n-2)

if __name__ == "__main__":
    n = 5
    print(solve(n))