def first_occur(nums, target, l):
    lo = 0
    hi = l
    while lo < hi:
        mid = lo + (hi-lo)//2
        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] >= target:
            hi = mid
    return lo


def is_majority_element(nums: list[int], target: int) -> bool:
    l = len(nums)
    first_index = first_occur(nums, target,l)
    minimum_last_index = first_index + l//2
    if minimum_last_index < l and nums[minimum_last_index] == target:
        return True
    return False


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 7, 12]
    print(is_majority_element(nums, 3))  # True
    print(is_majority_element(nums, 4))  # False
    print(is_majority_element(nums, 5))  # False
