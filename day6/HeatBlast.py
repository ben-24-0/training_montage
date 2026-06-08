def wildfire(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
        return
    grid[i][j]=2
    wildfire(grid,i+1,j)         #//D
    wildfire(grid,i-1,j)       #//U 
    wildfire(grid,i,j+1)     #//R   
    wildfire(grid,i,j-1)   #// L      

matrix = [[1,1,1,1],
[1,0,0,0],
[0,0,1,1],
[1,0,0,0]
]


wildfire(matrix,0,0)
count=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            count+=1
print(count)