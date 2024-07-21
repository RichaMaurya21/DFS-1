# DFS-1

## Problem1 (https://leetcode.com/problems/flood-fill/)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        
        if not image or image[sr][sc] == color:
            return image
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        startColor = image[sr][sc]

        q = deque([(sr, sc)])
        while q:
            r, c = q.popleft()
            image[r][c] = color
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nc >= 0 and nr < m and nc < n and image[nr][nc] == startColor:
                    q.append((nr,nc))

        return image


