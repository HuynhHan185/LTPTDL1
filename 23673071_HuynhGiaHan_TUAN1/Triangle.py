class Triangle:
    def __init__(self, bc, ab, ac, chieucao):
        self.bc = bc
        self.ab = ab
        self.ac = ac
        self.chieucao = chieucao
    
    def area(self):
        result = 1/2*self.bc*self.chieucao
        return result
    def perimeter(self):
        result = self.bc + self.ab + self.ac
        return result
    def display(self):
        print(f'canhbc: {self.bc}, canhab: {self.ab}, canhac: {self.ac}, chu vi: {self.perimeter():.2f}, diện tích: {self.area():.2f}\n')