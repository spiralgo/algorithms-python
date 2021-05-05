def get_sum_of_kth_power_digits(n, k):
    result = 0
    while n != 0:
        result += (n % 10)**k
        n //= 10
    return result


def armstrong_number(n: int) -> bool:
    k = len(str(n))
    return get_sum_of_kth_power_digits(n, k) == n


if __name__ == "__main__":
    print(armstrong_number(153))  # True
    print(armstrong_number(370))  # True
    print(armstrong_number(1634))  # True
    print(armstrong_number(85))  # False
    print(armstrong_number(101))  # False
