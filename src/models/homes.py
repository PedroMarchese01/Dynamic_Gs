
from random import randint


class Home:

    def __init__(self, battery=None):

        self.base_consumption = 3.0
        self.electricity_consumption = 3.0

        self.energy_received = 0.0
        self.total_electricity_consumption = 0.0

        self.energy_demand = 0.0
        self.is_attended = False

    def get_electricity_consumption(self):
        return self.electricity_consumption

    def get_total_electricity_consumption(self):
        return self.total_electricity_consumption

    def set_electricity_consumption(self, consumption):

        if consumption < 0:
            raise ValueError("Consumo inválido")

        self.base_consumption = consumption
        self.electricity_consumption = consumption

    def update_consumption(self):

        variation = randint(-30, 30) / 100

        self.electricity_consumption = (
            self.base_consumption * (1 + variation)
        )

    def get_energy_demand(self, interval_seconds=1):

        self.energy_demand = (
            self.electricity_consumption
            * interval_seconds / 3600
        )

        return self.energy_demand

    def set_energy_received(self, amount):

        self.energy_received = amount

        self.total_electricity_consumption += amount

        self.is_attended = (
            amount >= self.energy_demand - 0.0000001
        )
