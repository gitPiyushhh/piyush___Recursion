def solve(n, k):
    # 1. Base cases
    if n <= 1 and k <= 1: return 0
    
    # 2. Normal cases
    cur_nodes = 2**(n-1)
    
    #/ In prev range
    if k <= cur_nodes // 2:
        return solve(n-1, k)
    
    #/ Not in prev range
    else:
        return not solve(n-1, k-(cur_nodes // 2)) #/ '//2' coz we want nodes in prev


if __name__ == '__main__':
    print(solve(4, 7))