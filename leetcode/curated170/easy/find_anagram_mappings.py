class Solution:
    def anagramMappings(self, A: list[int], B: list[int]) -> list[int]:

        locations = {}
        for i in range(len(B)):
            locations[B[i]] = i
        mapping = []
        for x in A:
            mapping.append(locations[x])
        return mapping


if __name__ == "__main__":
    solution = Solution()
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    print(solution.anagramMappings(A, B))  # [1, 4, 3, 2, 0]
