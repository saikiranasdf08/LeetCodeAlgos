'''
322. Coin Change
https://leetcode.com/problems/coin-change/
'''

#DP minimum coin change
def knapsackUnbounded_TopDown(coins, wt, n):
    dp1 = [0] + [max] * wt
    print(dp1)
    dp=[[0 for i in range(wt+1)] for j in range(n+1)]
    infnity = float('inf')-1
    for i in range(wt+1):
        dp[0][i]=infnity
        if i%coins[0] == 0:
            dp[1][i]= i // coins[0]
        else:
            dp[1][i]=infnity

    print(dp)
    for i in range(2,n+1):
        for j in range(1,wt+1):
            if coins[i - 1]<=j:
                dp[i][j]=min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp)
    return dp[n][wt]

print(knapsackUnbounded_TopDown([2,3,5],4,3))