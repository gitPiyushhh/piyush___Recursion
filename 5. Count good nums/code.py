## Ques. We have to find all possible combinations of 3 digit where in odd places{prime nums}, even places{even nums}

def solve(n):
    
    # 1. Find the even and odd nums
    o = n // 2
    e = n - o
    
    # 2. Return the nums of choices //Coz we 5*5*5 == 5^3
    return 5**e * 4**o

if __name__ == '__main__':
    print(solve(3))