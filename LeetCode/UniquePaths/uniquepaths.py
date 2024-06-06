class Solution(object):
    
    def right(self, n, x, y, grid):
        # Check if moving right will go out of bounds
        if x+1 >= n:
            return 0 
        # Return the value at the cell to the right
        return grid[y][x + 1]

    
    def down(self, m, x, y, grid):
        # Check if moving down will go out of bounds
        if y+1 >= m:
            return 0 
        # Return the value at the cell below
        return grid[y + 1][x]

    def uniquePaths(self, m, n):
        # Create a grid of size m x n filled with zeros
        grid = [[0] * n for _ in range(m)]
        # Set the bottom-right cell to 1, as there is only one way to reach it
        grid[m-1][n-1] = 1
        # Traverse the grid from bottom-right to top-left
        for y in range(m-1, -1, -1):
            for x in range(n-1, -1, -1): 
                # Skip the bottom-right cell, as it has already been set to 1
                if x == n-1 and y == m-1:
                    continue
                # Calculate the number of unique paths to the current cell
                grid[y][x] = self.right(n, x, y, grid) + self.down(m, x, y, grid)
        # Return the number of unique paths to the top-left cell
        return grid[0][0]
        """
        :type m: int
        :type n: int
        :rtype: int
        """