import random

class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1):
                if (i % 2 == 0) == (nums[i] > nums[i + 1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == "__main__":
    A = []
    for _ in range(10):
        A.append(random.randint(1,20))
    print(A)

    solution = Solution()
    solution.wiggleSort(A)
    print(A)

