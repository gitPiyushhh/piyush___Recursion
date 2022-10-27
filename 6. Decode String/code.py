def solve(s, i):
    
    # 1. Base cases
    if i >= len(s): return 1    #/ No fault
    if s[i] == '0': return 0    #/ Fault found
    
    # 2. Normal cases
    left = solve(s, i+1)
    right = 0
    
    two_digit = int(s[i: i+2])  #/ In case if digits not available till i+2, then it will stop on len(arr) not matter it gets or ot i+2
    
    if 10 <= two_digit <= 26:
        right = solve(s, i+2)   #/ If possible then only call
    
    return left + right
    
    

if __name__ == '__main__':
    print(solve('11106', 0))