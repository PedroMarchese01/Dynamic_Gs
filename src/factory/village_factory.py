
from src.factory import graph_village_factory
from src.models.homes import Home
from src.models.battery_bank import BatteryBank


class VillageFactory:

    def __init__(self, battery: BatteryBank):

        self.battery = battery
        self.village = []
        self.graph = None

    def append_home(self, home):

        self.village.append(home)
        return True

    def append_number_of_home(self, number_of_home: int):

        for _ in range(number_of_home):

            new_home = Home(self.battery)
            self.village.append(new_home)

        return True

    def generate_graph(self):

        self.graph = graph_village_factory.generate(
            self.village
        )

        return self.graph

    def update_consumptions(self):

        for home in self.village:
            home.update_consumption()

    def get_homes(self):
        return self.village

    def get_total_homes(self):
        return len(self.village)

    def get_attended_homes(self):

        return sum(
            1 for home in self.village
            if home.is_attended
        )
