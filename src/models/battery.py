
class Battery:

    def __init__(self, capacity_wh=50, energy_wh=0):

        if capacity_wh <= 0:
            raise ValueError("Capacidade inválida")

        if not 0 <= energy_wh <= capacity_wh:
            raise ValueError("Energia inicial inválida")

        self.capacity_wh = capacity_wh
        self.energy_wh = energy_wh

    def charge(self, amount):
        if amount < 0:
            return False

        accepted = min(
            amount,
            self.capacity_wh - self.energy_wh
        )

        self.energy_wh += accepted
        return amount - accepted

    def discharge(self, amount):
        if amount < 0 or amount > self.energy_wh:
            return False

        self.energy_wh -= amount
        return True

    def get_level(self):
        return (self.energy_wh / self.capacity_wh) * 100

    def get_energy(self):
        return self.energy_wh

    def get_capacity(self):
        return self.capacity_wh
