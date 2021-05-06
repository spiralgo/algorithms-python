class Solution:
    def get_sum_of_kth_power_digits(self, n, k):
            result = 0
            while n != 0:
                result += (n % 10)**k
                n //= 10
            return result

    def isArmstrong(self, n: int) -> bool:
            k = len(str(n))
            return self.get_sum_of_kth_power_digits(n, k) == n   

if __name__ == '__main__':
     solution = Solution()
     print(solution.isArmstrong(153))  #True
     print(solution.isArmstrong(370))  # True
     print(solution.isArmstrong(1634))  # True
     print(solution.isArmstrong(85))  # False
     print(solution.isArmstrong(101))  # False