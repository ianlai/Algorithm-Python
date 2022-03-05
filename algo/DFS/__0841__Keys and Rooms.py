class Solution:
    
    #DFS [O(V+E): 71%]
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return []
        
        opened = [0] * len(rooms)
        opened[0] = 1
        visited = [0] * len(rooms)
        visited[0] = 1
        
        self.traverse(rooms, 0, opened, visited)
        numOpenedRoom = 0
        for i in range(len(rooms)):
            numOpenedRoom += opened[i]
        return numOpenedRoom == len(rooms)
    
    def traverse(self, rooms, cur, opened, visited):
        for key in rooms[cur]: 
            if visited[key] == 1:
                continue
                
            opened[key] = 1
            visited[key] = 1
            self.traverse(rooms, key, opened, visited)
                