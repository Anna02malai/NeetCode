class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while l < r and top < bottom:
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1

            if not (l <r and top < bottom):
                break

            for i in range(r -1, l- 1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1
        return res

def main():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    res = Solution()
    print(res.spiralOrder(matrix))

if __name__ == "__main__":
    main()