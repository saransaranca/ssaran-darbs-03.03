import requests
import matplotlib.pyplot as plt
from person_a import Book


class PaplašinātaGrāmata(Book):
    def __init__(self, nosaukums, autors, lapas, žanrs):
        super().__init__(nosaukums, autors, lapas)
        self.žanrs = žanrs
    

    def paradi_info(self):
        pamata_info = super().paradi_info()
        return f"{pamata_info}, Žanrs: {self.žanrs}"
    
    def iegut_gramatas_info_no_api(self):
        api_url = f"https://www.googleapis.com/books/v1/volumes?q={self.nosaukums}+inauthor:{self.autors}"
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200 and 'items' in data:
            grāmatas_info = data['items'][0]['volumeInfo']
            apraksts = grāmatas_info.get('description')
            return f"Grāmatas apraksts: {apraksts}"
        else:
            return "Neizdevās atrast informāciju par grāmatu."

    def paradi_lapas(self, grāmatas):
        """Grafiks lapu skaitam grāmatās."""
        nosaukumi = [grāmata.nosaukums for grāmata in grāmatas]
        lapas = [grāmata.lapas for grāmata in grāmatas]

        plt.figure(figsize=(10, 6))
        plt.bar(nosaukumi, lapas)
        plt.xlabel('Grāmatas nosaukums')
        plt.ylabel('Lapu skaits')
        plt.title('Lapu skaits grāmatās')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

