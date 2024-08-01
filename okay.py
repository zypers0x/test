from collections import deque

def min_bannermen_cost(n, m, grid, castle_x, castle_y):
    # Directions for moving in the grid: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS setup
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    cost = 0
    
    # Add all border cells to the queue
    for i in range(n):
        if grid[i][0] != 0:
            queue.append((i, 0))
            visited[i][0] = True
        if grid[i][m-1] != 0:
            queue.append((i, m-1))
            visited[i][m-1] = True

    for j in range(m):
        if grid[0][j] != 0:
            queue.append((0, j))
            visited[0][j] = True
        if grid[n-1][j] != 0:
            queue.append((n-1, j))
            visited[n-1][j] = True
    
    # BFS to mark all reachable cells from borders
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    # Calculate the minimum cost to block the reachable cells
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                cost += grid[i][j]
    
    return cost

# Read input
n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for _ in range(n)]
castle_x, castle_y = map(int, input().strip().split())

# Compute and print the result
result = min_bannermen_cost(n, m, grid, castle_x, castle_y)
print(result)
