def maze (grid,path,i,j):
    if i==n and j==n:
        print(path)
        return
    if i+1 <=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j)
    if j+1 <=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1)
    

grid = [
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
n = len(grid) - 1

maze(grid, "", 0, 0)