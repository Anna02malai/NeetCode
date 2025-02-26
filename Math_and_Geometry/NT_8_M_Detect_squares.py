from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: list[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: list[int]) -> int:
        res = 0
        qx, qy = point

        for x, y in self.pts:
            if (abs(y - qy) != abs(x - qx) or x == qx or y == qy):
                continue
            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)]        
        return res

def main():
    inp = ["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]
    res = CountSquares()

if __name__ == "__main__":
    main()
