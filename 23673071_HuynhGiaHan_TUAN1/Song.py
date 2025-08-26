class Song:
    def __init__(self, code, title, singer, genre, year, views):
        self.code = code
        self.title = title
        self.singer = singer
        self.genre = genre
        self.year = year
        self.views = views
    def display(self):
        print(f"{self.code} - {self.title} - {self.singer} - {self.genre} - {self.year} - {self.views}")
    
    def increaseViews(self, amount):
        if amount > 0:
            self.views += amount
            
    def decreaseViews(self, amount):
        if amount > 0 and self.views - amount >= 0:
            self.views -= amount
    