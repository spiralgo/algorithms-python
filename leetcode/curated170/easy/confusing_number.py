class Solution:
    def confusingNumber(self, N: int) -> bool:
        map = {6: 9, 9: 6, 0: 0, 1: 1, 8: 8}
        new_num = 0
        x = N
        while x != 0:
            remainder = x % 10
            if remainder not in map:
                return False
            new_num = new_num*10 + map[remainder]
            x //= 10
        return N != new_num


if __name__ == "__main__":
    s = Solution()
    print(s.confusingNumber(86))  # True
    print(s.confusingNumber(11))  # False
    print(s.confusingNumber(99))  # True
    print(s.confusingNumber(181))  # False
    print(s.confusingNumber(939))  # False
    print(s.confusingNumber(8018))  # True
