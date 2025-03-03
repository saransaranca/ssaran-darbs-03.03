class Object:
    def __init__(self, name):
     self.name = name
    def paradi_info(self):
        return f"objekts: {self.name}"
class Book(Object):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages
    def paradi_info(self):
        return f"Grāmata: {self.name}, Autors: {self.author}, lapaspuses: {self.pages}"

