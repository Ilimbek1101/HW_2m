# ExtraTask:

class Solution:

    def maximum_wealth(self, account):
        self.account = account
        for i in account:
            money = 0
            richest = 0
            for j in i:
                money += j
            if richest < money:
                richest = money

        print(f'Самый богатый клиент имеет ${richest}.')

account = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
a = Solution()
a.maximum_wealth(account)