class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        tr = 0
        br = rows - 1        

        while tr <= br:
            row = (tr + br)//2
            if matrix[row][-1] < target:
                tr = row + 1
            elif matrix[row][0] > target:
                br = row - 1
            else :
                break

        if not(tr <= br):
            return False

        l, r = 0, cols - 1
        while l <= r:
            col = (l + r)//2
            if matrix[row][col] > target:
                r = col -1
            elif matrix[row][col] < target:
                l = col +1
            else:
                return True
        return False

def main():
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    res = Solution()
    print(res.searchMatrix(matrix, target))

if __name__ == "__main__":
    main()

