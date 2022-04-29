# Выполнение домашнего задания 6, ООП (2 месяц).
# Бинарный поиск.

def get_list():
    nums = list(range(0, 10000000, 2))
    return nums

class Solution:

    def find_target(self, nums, target):
        n = 0
        low = 0
        high = len(nums) - 1
        mid = int((low + high) / 2)
        # print(target)
        # print(low, high, mid, nums[mid], nums[low], nums[high])
        while high - low > 1:
            if target > nums[mid]:
                low = mid
                mid = int((low + high)/2)
                n += 1
            elif target < nums[mid]:
                high = mid
                mid = int((low + high)/2)
                n += 1
            else:
                print(f'Число {target} есть в массиве под индексом {mid}, '
                      f'понадобилось {n} итераций для его нахождения')
                break

find = Solution()
nums = get_list()
find.find_target(nums, 45866)

