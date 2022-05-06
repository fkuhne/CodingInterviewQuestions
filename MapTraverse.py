# https://youtu.be/oBt53YbR9Kk?t=3898
# Count the number of ways to move through a n x m grid

def dp(n, m, memo = {}):
    # base cases
    if 0 in {n, m}: return 0
    if n == 1 and m == 1: return 1
    
    key = "{},{}".format(n, m)
    if key in memo: return memo[key]
    
    memo[key] = dp(n-1, m, memo) + dp(n, m-1, memo)
    return memo[key]

print(dp(1, 1))
print(dp(2, 3))
print(dp(3, 2))
print(dp(10, 10))
print(dp(400, 400))
