def solve(arr, l, r, y):
    # 1. Base cases
    if l == r: return arr[l] * y
    
    # 2. Normal cases
    left = arr[l] * y + solve(arr, l+1, r, y+1)
    right = arr[r] * y + solve(arr, l, r-1, y+1)

    return max(left, right)


if __name__ == '__main__':
    arr = [2, 3, 5, 1, 4]
    print(solve(arr, 0, len(arr)-1, 1))