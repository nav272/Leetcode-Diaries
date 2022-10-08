from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        myqueue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                #mark the number of zeros
                if matrix[i][j] == 0:
                    myqueue.append((i, j))
                    #keep track of visited 
                    visited.add((i, j))
        
        while myqueue:
            x, y = myqueue.popleft()
            #going in the 4 directions from the current index
            for i, j in [(0,1), (0,-1), (-1, 0), (1,0)]:
                newX, newY = x+i, y+j
                if newX>=0 and newX< m and newY >= 0 and newY < n and newY >=0 and (newX, newY) not in visited:
                     matrix[newX][newY] = matrix[x][y] + 1
                     myqueue.append((newX, newY))
                     visited.add((newX, newY))
        
        return matrix
