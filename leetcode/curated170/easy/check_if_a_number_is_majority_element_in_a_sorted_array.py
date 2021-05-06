class Solution:
   def isMajorityElement(self, nums: list[int], target: int) -> bool:
           l = len(nums)
           first_index = self.first_occur(nums, target,l)
           minimum_last_index = first_index + l//2
           if minimum_last_index < l and nums[minimum_last_index] == target:
               return True
           return False
       
   def first_occur(self, nums, target, l):
       lo = 0
       hi = l
       while lo < hi:
           mid = lo + (hi-lo)//2
           if nums[mid] < target:
               lo = mid + 1
           elif nums[mid] >= target:
               hi = mid
       return lo


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 7, 12]
    s = Solution()
    print(s.isMajorityElement(nums, 3))  # True
    print(s.isMajorityElement(nums, 4))  # False
    print(s.isMajorityElement(nums, 5))  # False
