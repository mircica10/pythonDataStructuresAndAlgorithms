"""
https://www.infoarena.ro/problema/ferma3
"""


class Cell():
    def __init__(self, color):
        self.color = color
        self.visited = False
        self.id = 0
        
class Farm():
    def __init__(self, farm):
        self.farm = farm
        self.m = len(farm[0])
        self.n = len(farm)
        self.cells = []
        self.max_areas = {}
        self.initCells()
    
    def initCells(self):
        self.cells = [[None for _ in range(self.m)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                self.cells[i][j] = Cell(self.farm[i][j])
    
    def validPosition(self, color, i, j):
        return (i >= 0 and i < self.n and
                j >= 0 and j < self.m and
                self.cells[i][j].visited == False and
                self.cells[i][j].color == color)


    def calculateMaxArea(self):
        max_area = 0

        self.calculateParcelAreas()
        
        for area in self.max_areas:
            max_area = max(max_area, self.max_areas[area])
        return max_area


    def calculateParcelAreas(self):
        for i in range(self.n):
            for j in range(self.m):
                id = self.getUniqueId(i, j)
                if self.cells[i][j].visited == False:
                    self.calculateParcelArea(self.cells[i][j].color, i, j, id)

    def getUniqueId(self, i, j):
        return i * 37 + j
    
    def calculateParcelArea(self, color, i, j, id):
        max_area = self.floodFill(color, i, j, id)
                
        self.max_areas[id] = max_area
        self.cells[i][j].id = id

    def floodFill(self, color, i, j, id):
        if not self.validPosition(color, i, j):
            return 0

        self.cells[i][j].visited = True
        self.cells[i][j].id = id        
        
        area = 1 + self.floodFill(color, i - 1, j, id) + self.floodFill(color, i + 1, j, id) +\
            self.floodFill(color, i, j - 1, id) + self.floodFill(color, i, j + 1, id)
        return area
    
    def calculateMaxAreaModified(self):
        max_area_modified = 0
        for i in range(self.n):
            for j in range(self.m):
                colors_next = {}
                checked_ids = []
                color = self.cells[i][j].color
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for direction in directions:
                    i_new = i + direction[0]
                    j_new = j + direction[1]
                    
                    if (i_new >= 0 and i_new < self.n and
                            j_new >= 0 and j_new < self.m and
                            self.cells[i_new][j_new].color != color):
                        curr_color = self.cells[i_new][j_new].color
                        curr_id = self.cells[i_new][j_new].id
                        
                        if curr_color in colors_next and curr_id not in checked_ids:
                            colors_next[curr_color] += self.max_areas[curr_id]#self.cells[i_new][j_new].area
                        else:
                            colors_next[curr_color] = self.max_areas[curr_id]#self.cells[i_new][j_new].area
                        checked_ids.append(curr_id)
    
                for c in colors_next:
                    max_area_modified = max(colors_next[c] + 1, max_area_modified)
        return max_area_modified    
    
    def solve(self):
        max_area = self.calculateMaxArea()
        max_area_modified = self.calculateMaxAreaModified()
        return (max_area, max_area_modified)

def test():
    farm = [
        list("rmmgggaa"),
        list("mvvgggaa"),
        list("mvvgvvvv"),
        list("vvvrvvvv"),
        list("vvrrrgga"),
        list("vvrrrggg"),
        list("aaaaaaag")
    ]
    f = Farm(farm)
    (max_area, max_area_modified) = f.solve()
    assert(max_area == 11)
    assert(max_area_modified == 20)
    
test()