from collections import deque
from typing import List

class Solution:

    # 2025/01/18 ChatGPT檢查過 
    # 去掉visited
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 檢查 image 是否有效
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return image
        
        color_original = image[sr][sc]
        if color_original == color:  # 如果起始顏色和目標顏色相同，直接返回
            return image

        deq = deque([(sr, sc)])
        while deq:
            r, c = deq.popleft()
            image[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # 檢查是否不在矩陣內
                if not (0 <= nr < len(image) and 0 <= nc < len(image[0])):
                    continue
                # 檢查顏色是否符合條件
                if image[nr][nc] != color_original:
                    continue
                deq.append((nr, nc))
        
        return image


    # 2025/01/16 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return image

        color_original = image[sr][sc]
        deq = deque([(sr, sc)])
        visited = set([sr, sc])
        while deq: 
            r, c = deq.popleft() 
            image[r][c] = color
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if not(0 <= nr < len(image) and 0 <= nc < len(image[0])):
                    continue
                if image[nr][nc] != color_original:
                    continue
                if (nr, nc) in visited:
                    continue
                deq.append((nr, nc))
                visited.add((nr, nc))
        return image
                