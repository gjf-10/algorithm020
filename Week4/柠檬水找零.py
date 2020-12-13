class Solution:
    def lemonadeChange(self, bills) -> bool:
        # 在收到钱时，如果需要找零则在收到的钱里用贪心有大找大，如果找不开则返回False
        res = {'5':0, '10':0}
        for price in bills:
            if price == 5:
                res[str(price)] += 1
            elif price == 10:
                if res['5'] > 0:
                    res[str(price)] += 1
                    res['5'] -= 1
                else:
                    return False
            else:
                if res['10'] > 0 and res['5'] > 0:
                    res['10'] -= 1
                    res['5'] -= 1
                elif res['5'] >= 3:
                    res['5'] -= 3
                else:
                    return False
        return True