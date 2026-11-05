from src.models.battery import Battery
class BaterryBank:

    def __init__(self):
        self.power = []

    def append_battery(self, battery_amount):
        for i in range(battery_amount):
            new_battery = Battery(0)
            self.power.append(new_battery)

        return True

    def get_batteries_level(self):
        if not self.power:
            return 0
        return self.power[0].battery_level

    def charge(self, amount):
        if not self.power or amount < 0:
            return False

        if amount == 0:
            return True

        if amount >= 100 * len(self.power):
            ch_value = 100

        else:
            ch_value = amount / len(self.power)


        for bt in self.power:
            bt.charge(ch_value)
        return True

    def discharge(self, amount):
        if not self.power or amount < 0:
            return False

        if amount > self.get_batteries_level() * len(self.power):
            return False

        discharge_value = amount / len(self.power)

        for bt in self.power:
            bt.discharge(discharge_value)

        return True