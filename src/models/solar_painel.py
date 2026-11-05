from time import time, sleep
from threading import Thread

class SolarPainel:

    MAX_POWER = 550
    EFFICIENCY = 0.90
    BATTERY_CAPACITY = 50  # Wh por pilha

    def __init__(self, battery_bank, percent_initial_lighting):
        self.energy_target = battery_bank

        if not 0 <= percent_initial_lighting <= 100:
            raise ValueError("Luminosidade precisa estar entre 0 e 100")

        self.light = percent_initial_lighting
        self.running = False
        self.thread = None

    def light_change(self, new_light_value):
        if not 0 <= new_light_value <= 100:
            raise ValueError("Luminosidade precisa estar entre 0 e 100")

        self.light = new_light_value

    def turn_on(self):
        if self.running:
            return

        self.running = True
        self.thread = Thread(target=self.capture_sun_light)
        self.thread.start()

    def turn_off(self):
        self.running = False

    def capture_sun_light(self):
        last_update = time()

        while self.running:
            current_time = time()

            elapsed_time = current_time - last_update
            last_update = current_time

            if self.light > 0 and self.energy_target.power:

                energy_generated = (
                    self.MAX_POWER
                    * (self.light / 100)
                    * (elapsed_time / 3600)
                    * self.EFFICIENCY
                )

                capacity_total = (
                    len(self.energy_target.power)
                    * self.BATTERY_CAPACITY
                )

                percent_generated = (
                    energy_generated / capacity_total
                ) * 100

                self.energy_target.charge(percent_generated)

            sleep(1)