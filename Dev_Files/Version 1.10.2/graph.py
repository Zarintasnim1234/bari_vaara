# graph.py
import matplotlib.pyplot as plt

class Graph:
    @staticmethod
    def generate_rent_graph():
        locations = ['Downtown', 'Suburbs', 'City Center']
        rents = [1000, 1200, 1500]

        plt.bar(locations, rents)
        plt.title('Rent Prices by Location')
        plt.xlabel('Location')
        plt.ylabel('Rent')
        plt.show()
