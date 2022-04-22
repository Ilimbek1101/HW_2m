# ExtraTask 5:
# Дан массив целых чисел nums, отсортированных в порядке возрастания,
# и целое число target, напишите функцию для поиска target в nums.
# Если target существует, верните его индекс.
# В противном случае возвращайте -1.

nums = [ 23, 15, -6, 0, 85, -32, 46, 1, 8, 4]

nums.sort()
print(nums)

target = int(input('Введите искомое число: '))

s = 0
for i in nums:
    if i == target:
        print(f'Число {target} есть в списке с индексом {nums.index(i)}')
        s = 1
if s == 0:
    print(-1)
