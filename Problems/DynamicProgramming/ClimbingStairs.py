
def climbStairs( n):

    if n<3:
        return n
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

# return countcoins([1,2],n,2)

# DP
def countcoins(arr,wt,n):
    dp=[0 for i in range(wt+1) for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,wt+1):
            if arr[i-1]<=j:
                dp[i][j] = dp[i][j - arr[i-1]] + dp[i-1][j]
            else :
                dp[i][j]=dp[i-1][j]
    return dp[n][wt]