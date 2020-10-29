class Category:
    def _init_(self, categoryName):
        self.name = categoryName
        self.weight = 0
    
    def setWeight(self, percentage):
        self.weight = int(percentage)