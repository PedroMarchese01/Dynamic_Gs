
from src.factory import graph_village_factory
from src.models.homes import Home
class VillageFac():
    def __init__(self):
        self.village = []
        self.graph = []

    def append_home(self, home):
        self.village.append(home)
        return True

    def append_number_of_home(self, number_of_home:int):
        for _ in range(number_of_home):
            new_home = Home()
            self.village.append(new_home)

    def generate_graph(self):
        self.graph = graph_village_factory.generate(self.village)
        return self.graph

    def start_consume(self):
        for home in self.village:
            home.start_consumption()

    def stop_consume(self):
        for home in self.village:
            home.stop_consumption()