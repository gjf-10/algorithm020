class Solution:
    def numDecoding(self,s):
        if not s:
            return 0
        dp = [1] + [0] * len(s)
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

class Solution1:
    def numDecodings(self, s: str) -> int:
        # 子问题 找子集 0，>26, x0
        # f(n) = f(n-1) + f(n-2) 去掉不合理
        helper = {'10': 1, '20': 1}
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if len(s) <= 2:
            if int(s) > 26:
                if int(s) % 10 == 0:
                    return 0
                return 1
            elif helper.get(s):
                return 1
            else:
                return 2
        dp = [1] * len(s)
        for i in range(2):
            new_s = s[:i+1]
            if int(new_s) > 26:
                if int(new_s) % 10 == 0:
                    return 0
                dp[1] = 1
            elif helper.get(new_s):
                dp[1] = dp[0] = 1
            else:
                dp[1] = 2
        for i in range(2, len(s)):
            if s[i-1] != '0':
                new_s = s[i-1] + s[i]
                if helper.get(new_s):
                    dp[i] = dp[i-2]
                    dp[i-1] -= 1
                elif int(new_s) > 26:
                    if s[i] == '0':
                        return 0
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-2] + dp[i-1]
            else:
                if s[i] == '0':
                    return 0
                dp[i] = dp[i-1]
        return dp[-1]