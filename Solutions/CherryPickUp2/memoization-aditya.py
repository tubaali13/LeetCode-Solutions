class CherryPicker:
    def maxCherries(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memoization_cache = {}

        def explorePath(row, col1, col2):
            if (row, col1, col2) in memoization_cache:
                return memoization_cache[(row, col1, col2)]

            if col1 == col2 or min(col1, col2) < 0 or max(col1, col2) == cols:
                return 0

            if row == rows - 1:
                return grid[row][col1] + grid[row][col2]

            maxCherries = 0
            for move1 in [-1, 0, 1]:
                for move2 in [-1, 0, 1]:
                    maxCherries = max(
                        maxCherries,
                        explorePath(row + 1, col1 + move1, col2 + move2)
                    )

            memoization_cache[(row, col1, col2)] = maxCherries + grid[row][col1] + grid[row][col2]
            return memoization_cache[(row, col1, col2)]

        return explorePath(0, 0, cols - 1)
