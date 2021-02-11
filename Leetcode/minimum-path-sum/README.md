<https://leetcode.com/problems/minimum-path-sum>

이차원 배열 dp의 i, j 좌표의 값 : 이 지점까지의 최소값

즉, dp[i][j] = min(dp[i-1][j], dp[j-1][i]) + grid[i][j] 점화식이 성립한다 (단, i == 0 혹은 j = 0이 아닐때)