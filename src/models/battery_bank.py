
import threading

from src.models.battery import Battery


class BaterryBank:

    def __init__(self):
        self.power = []
        self.lock = threading.RLock()

    def append_battery(self, battery_amount: int):

        with self.lock:
            for _ in range(battery_amount):
                self.power.append(Battery(50))

        return True

    def charge(self, amount):

        if amount < 0:
            return False

        with self.lock:

            remaining = amount

            while remaining > 0.0000001:

                available = [
                    bt for bt in self.power
                    if bt.get_energy() < bt.get_capacity()
                ]

                if not available:
                    break

                share = remaining / len(available)
                accepted_total = 0

                for bt in available:
                    overflow = bt.charge(share)
                    accepted_total += share - overflow

                if accepted_total <= 0:
                    break

                remaining -= accepted_total

            return True

    def discharge(self, amount):

        if amount < 0:
            return False

        with self.lock:

            if amount > self.get_total_energy():
                return False

            remaining = amount

            for bt in self.power:

                available = bt.get_energy()
                withdrawal = min(available, remaining)

                bt.discharge(withdrawal)
                remaining -= withdrawal

                if remaining <= 0.0000001:
                    break

            return True

    def get_total_energy(self):

        with self.lock:
            return sum(bt.get_energy() for bt in self.power)

    def get_total_capacity(self):

        with self.lock:
            return sum(bt.get_capacity() for bt in self.power)

    def get_batteries_level(self):

        with self.lock:

            capacity = self.get_total_capacity()

            if capacity == 0:
                return 0

            return (
                self.get_total_energy() / capacity
            ) * 100

    def get_available_energy(self):
        return self.get_total_energy()
