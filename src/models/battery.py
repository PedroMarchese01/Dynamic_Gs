class Battery:

    """
        classe bateria

        criada para poder representar a energia armazenada em nosso sistema
        Ela necessariamente vai estar representada em porcentagem de 0 - 100%

        incialização:

        battery = Battery(valor)

        funções

        charge: recarrega o valor da bateria
        battery.charge(100)

        discharge: retira porcentagem de energia do valor da bateria
        battery.discharge(100)

        get_level: retorna o valor da bateria
        battery.get_level()
    """



    def __init__(self, battery_level):
        if not 0 <= battery_level <= 100:
            raise ValueError("Nível de bateria inválido")

        self.battery_level = battery_level

    def charge(self, amount):
        if amount < 0:
            return False

        self.battery_level = min(100, self.battery_level + amount)
        return True

    def discharge(self, amount):
        if amount < 0 or amount > self.battery_level:
            return False

        self.battery_level -= amount
        return True

    def get_level(self):
        return self.battery_level