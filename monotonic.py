nums = [1,2,2,3]
def non_increasing(nums):
    return all(i>=j for i, j in zip(nums, nums[1:]))

def non_decreasing(nums):
    return all(i<=j for i, j in zip(nums, nums[1:]))

def monotonic(nums):
    return non_increasing(nums) or non_decreasing(nums)
print(monotonic(nums))
