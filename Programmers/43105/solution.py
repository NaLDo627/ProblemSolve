import copy

def solution(triangle):
    answer = 0
    dp = copy.deepcopy(triangle)
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = 0

    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j], dp[i][j])
            answer = max(answer, dp[i][j])

    return answer


from unittest import TestCase

class Test(TestCase):
    def test_solution(self):
        self.assertEqual(30, solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

