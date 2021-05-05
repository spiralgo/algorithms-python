def confusing_number(n: int) -> bool:
    map = {6: 9, 9: 6, 0: 0, 1: 1, 8: 8}
    new_num = 0
    x = n
    while x != 0:
        remainder = x % 10
        if remainder not in map:
            return False
        new_num = new_num*10 + map[remainder]
        x //= 10
    return n != new_num


if __name__ == "__main__":
    print(confusing_number(86))  # True
    print(confusing_number(11))  # False
    print(confusing_number(99))  # True
    print(confusing_number(181))  # False
    print(confusing_number(939))  # False
    print(confusing_number(8018))  # True
