import random

def wiggle_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
            if (i % 2 == 0) == (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


if __name__ == "__main__":
    A = []
    for _ in range(10):
        A.append(random.randint(1,20))
    print(A)
    wiggle_sort(A)
    print(A)

