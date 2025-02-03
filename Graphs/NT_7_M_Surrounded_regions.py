class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r<0 or c<0 or r == rows or c == cols or board[r][c]!= "O"):
                return 
            
            board[r][c] = "T"
            capture(r+1, c)
            capture(r-11, c)
            capture(r, c+1)
            capture(r, c-1)

        #capture unsurrounded regions as T
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1])):
                    capture(r, c)

        #capture the surrounded regions 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #uncapture the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "T"):
                    board[r][c] = "O"

        return board
    
def main():
    board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"]
            ]
    res = Solution()
    print(res.solve(board))

if __name__ == "__main__":
    main()