def solve(arr, i, cur_cap):
    # 1. Base cases
    if cur_cap == 0: return True
    if i == len(arr) : return False #/ We still cant find
    
    # 2. Normal cases
    ##// Not-Considerable
    if arr[i] > cur_cap: return solve(arr, i+1, cur_cap)
    
    else:
        left = solve(arr, i+1, cur_cap) #/Not take
        right = solve(arr, i+1, cur_cap-arr[i]) #/Take
        
        return left or right

if __name__ == '__main__':
    arr = [5, 6, 3, 1, 0]
    
    print(solve(arr, 0, 7))