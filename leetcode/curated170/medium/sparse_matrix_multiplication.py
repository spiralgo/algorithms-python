class Solution:
       def multiply(self, a, b):
        nrowa = len(a)
        ncola = len(a[0])
        ncolb = len(b[0])
        # assertion, ncola==nrowb
        c = [[0] * ncolb for x in range(nrowa)]
        for i in range(nrowa):
            for k in range(ncola):
                if a[i][k] != 0:
                    for j in range(ncolb):
                        c[i][j] += a[i][k] * b[k][j]
        return c


if __name__ == "__main__":
    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]
    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    solution = Solution()
    c = solution.multiply(A, B)
    print(c) # [[7, 0, 0], [-7, 0, 3]]
