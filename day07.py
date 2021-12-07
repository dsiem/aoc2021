from math import ceil, floor

with open('day07.txt', encoding='utf8') as file:
    nums = sorted(map(int, file.read().split(',')))

median = nums[len(nums) // 2] # high median
print(sum(abs(n - median) for n in nums))

triangle = lambda n: n * (n + 1) // 2
mean = sum(nums) / len(nums)
print(min(sum(triangle(abs(n - m)) for n in nums) for m in (floor(mean), ceil(mean))))
