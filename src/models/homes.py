
import threading
from random import randint


class Home:
    def __init__(self):
        self.electricity_consumption = 0
        self.total_electricity_consumption = 0

        self.consumption_is_defined = False

        self.stop_event = threading.Event()
        self.consumption_thread = None

    def get_electricity_consumption(self):
        return self.electricity_consumption

    def get_total_electricity_consumption(self):
        return self.total_electricity_consumption

    def set_electricity_consumption(self, consumption: float):
        self.electricity_consumption = consumption
        self.consumption_is_defined = True
        return True

    def consume_electricity(self):
        interval_counter = 5
        electricity_usage = 0

        while not self.stop_event.is_set():

            if interval_counter == 5 and not self.consumption_is_defined:
                interval_counter = 0
                electricity_usage = randint(0, 5)

            self.total_electricity_consumption += electricity_usage

            #=================

            # lógica do gerador

            #=================

            interval_counter += 1

            self.stop_event.wait(1)

    def start_consumption(self):
        if self.consumption_thread and self.consumption_thread.is_alive():
            return

        self.stop_event.clear()

        self.consumption_thread = threading.Thread(
            target=self.consume_electricity
        )

        self.consumption_thread.start()

    def stop_consumption(self):
        self.stop_event.set()

        if self.consumption_thread and self.consumption_thread.is_alive():
            self.consumption_thread.join()
