'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.


Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4


Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.


Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[r][c] is only 0, 1, or 2.

'''

class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1

        queue = []
        freshOranges = 0
        minutes = 0

        row = len(grid)
        column = len(grid[0])
        
        for r in range(row):
            for c in range(column):
                if grid[r][c] == 2: # rotten oranges 
                    queue.append((r, c, 0))
                
                if grid[r][c] == 1: # fresh oranges 
                    freshOranges += 1
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while queue:
            Row, Column, minutes = queue.pop(0)
            
            for dirn in directions:
                ro, col = Row + dirn[0], Column + dirn[1] 

                if row > ro >= 0 and column > col >= 0 and grid[ro][col] == 1:
                    queue.append((ro, col, minutes+1))
                    grid[ro][col] = 2
                    freshOranges = freshOranges - 1
        
        if freshOranges > 0: # cannot rot all oranges 
            return -1
        
        return minutes 

sol = Solution()
grid1 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
    ]
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(grid)) 