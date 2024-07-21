## Problem2 (https://leetcode.com/problems/01-matrix/)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        direction = ((1,0),(0,1),(-1,0),(0,-1))

        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = float('inf')

        while q:
                r,c = q.popleft()
                for dr,dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nc >= 0 and nr < m and nc < n and mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr,nc))


        return mat

                


        
        


