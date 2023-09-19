def two_sum(array, target):
    if type(array) not in [list]:
        raise TypeError('array is not list')
    if type(target) not in [int, float]:
        raise TypeError('target is not integer or float')
    nums = sorted(array)
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            a = array.index(nums[left])
            return [array.pop(a), array.index(nums[right]), array.insert(a, nums[left])]

        elif sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


