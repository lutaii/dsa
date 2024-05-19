
def binarySearch(nums, target) -> bool:
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        m = lo + (hi - lo) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            hi = m - 1
        else:
            lo = m + 1
    return False

print(binarySearch(nums= [1,2,4,5],target= 5))