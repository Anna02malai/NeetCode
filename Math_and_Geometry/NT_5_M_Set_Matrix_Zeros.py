class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                        row_zero = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        for r in range(rows):
            if matrix[0][0] == 0:
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        return matrix

def main():
    matrix = [
            [1,2,3],
            [4,0,5],
            [6,7,8]
            ]
    res = Solution()
    print(res.setZeroes(matrix))

if __name__ == "__main__":
    main()