
from time import time
from threading import Thread, Event

from src.models.battery_bank import BatteryBank


class SolarPanel:

    MAX_POWER = 550
    EFFICIENCY = 0.90

    def __init__(
        self,
        battery_bank: BatteryBank,
        percent_initial_lighting
    ):

        if not 0 <= percent_initial_lighting <= 100:
            raise ValueError("Luminosidade inválida")

        self.energy_target = battery_bank
        self.light = percent_initial_lighting

        self.running = False
        self.thread = None
        self.stop_event = Event()

    def light_change(self, new_light_value):

        if not 0 <= new_light_value <= 100:
            raise ValueError("Luminosidade inválida")

        self.light = new_light_value

    def turn_on(self):

        if self.running:
            return

        self.running = True
        self.stop_event.clear()

        self.thread = Thread(
            target=self.capture_sun_light
        )

        self.thread.start()

    def turn_off(self):

        self.running = False
        self.stop_event.set()

        if self.thread and self.thread.is_alive():
            self.thread.join()

    def capture_sun_light(self):

        last_update = time()

        while not self.stop_event.is_set():

            current_time = time()

            elapsed_time = current_time - last_update
            last_update = current_time

            if self.light > 0:

                energy_generated = (
                    self.MAX_POWER
                    * (self.light / 100)
                    * (elapsed_time / 3600)
                    * self.EFFICIENCY
                )

                self.energy_target.charge(
                    energy_generated
                )

            self.stop_event.wait(1)
