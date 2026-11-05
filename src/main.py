from time import sleep

from src.models.battery_bank import BaterryBank
from src.models.solar_painel import SolarPainel


def main():
    # Criando banco com 10 pilhas de 50 Wh
    battery_bank = BaterryBank()

    battery_bank.append_battery(10)

    # Criando painel solar com luminosidade inicial de 80%
    solar_panel = SolarPainel(battery_bank, 80)

    print("=== SIMULAÇÃO SOLAR ===")
    print(f"Quantidade de pilhas: {len(battery_bank.power)}")
    print(f"Carga inicial: {battery_bank.get_batteries_level()}%")

    # Iniciando captação
    solar_panel.turn_on()

    try:
        for second in range(1, 31):
            sleep(1)

            # Simulando consumo após 10 segundos
            if second == 10:
                print("\n[CONSUMO] Casa consumindo 5% do banco")
                battery_bank.discharge(5)

            # Alterando luminosidade após 15 segundos
            if second == 15:
                print("\n[CLIMA] Luminosidade reduzida para 40%")
                solar_panel.light_change(40)

            # Exibindo informações
            print(
                f"Segundo: {second:02d} | "
                f"Luminosidade: {solar_panel.light}% | "
                f"Carga média: {battery_bank.get_batteries_level():.4f}%"
            )

    finally:
        solar_panel.turn_off()

    print("\n=== RESULTADO FINAL ===")
    print(f"Carga final: {battery_bank.get_batteries_level():.4f}%")
    print("Simulação encerrada.")


if __name__ == "__main__":
    main()