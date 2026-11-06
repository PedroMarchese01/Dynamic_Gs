
from time import sleep, time

from src.models.battery_bank import BaterryBank
from src.models.solar_painel import SolarPainel
from src.factory.village_factory import VillageFac
from src.service.energy_distribution import EnergyDistribution
from src.service.live_village_view import LiveVillageView


# =====================================
# CONFIGURAÇÕES
# =====================================

NUMBER_OF_BATTERIES = 10
NUMBER_OF_HOMES = 30

NIGHT_HOURS = 12
NIGHT_DURATION_SECONDS = 120

# 12 horas simuladas em 120 segundos reais.
NIGHT_STEP_SECONDS = (
    NIGHT_HOURS * 3600 / NIGHT_DURATION_SECONDS
)

EDGE_CAPACITY_W = 1000


# =====================================
# FUNÇÕES AUXILIARES
# =====================================

def show_final_result(battery_bank, homes):

    attended = sum(
        1 for home in homes
        if getattr(home, "is_attended", False)
    )

    total = len(homes)

    print("\n")
    print("=" * 45)
    print("           RESULTADO DA SIMULAÇÃO")
    print("=" * 45)

    print(f"Casas atendidas: {attended}/{total}")

    print(
        f"Bateria restante: "
        f"{battery_bank.get_batteries_level():.2f}%"
    )

    print(
        f"Energia armazenada: "
        f"{battery_bank.get_available_energy():.2f} Wh"
    )

    print("=" * 45)


# =====================================
# MAIN
# =====================================

def main():

    print("=" * 45)
    print("       SISTEMA DE DISTRIBUIÇÃO DE ENERGIA")
    print("=" * 45)

    print("\n1 - Simulação normal")
    print("2 - Simular uma noite (12 horas)")

    option = input("\nEscolha o modo: ").strip()

    if option not in ("1", "2"):
        print("Opção inválida.")
        return

    night_mode = option == "2"

    mode = "NOTURNO" if night_mode else "NORMAL"

    # =====================================
    # BANCO DE BATERIAS
    # =====================================

    battery_bank = BaterryBank()

    battery_bank.append_battery(
        NUMBER_OF_BATTERIES
    )

    # Na simulação noturna, começa com 100%.
    if night_mode:

        battery_bank.charge(
            battery_bank.get_total_capacity()
        )

    # =====================================
    # PAINEL SOLAR
    # =====================================

    solar_panel = SolarPainel(
        battery_bank,
        percent_initial_lighting=80
    )

    # =====================================
    # CRIAÇÃO DA VILA
    # =====================================

    village = VillageFac(battery_bank)

    village.append_number_of_home(
        NUMBER_OF_HOMES
    )

    homes = village.get_homes()

    # Define o consumo inicial das casas.
    for i, home in enumerate(homes):

        home.set_electricity_consumption(
            2 + (i % 9)
        )

    # =====================================
    # GERAÇÃO DO GRAFO
    # =====================================

    graph = village.generate_graph()

    print("\nGrafo gerado.")
    print(f"Casas: {len(homes)}")
    print(f"Conexões iniciais: {graph.number_of_edges()}")

    # =====================================
    # DISTRIBUIDOR DE ENERGIA
    # =====================================

    distributor = EnergyDistribution(
        battery_bank,
        village,
        edge_capacity_w=EDGE_CAPACITY_W
    )

    # =====================================
    # VISUALIZAÇÃO AO VIVO
    # =====================================

    viewer = LiveVillageView(
        graph,
        homes,
        distributor.source_node
    )

    # =====================================
    # INICIALIZAÇÃO
    # =====================================

    if night_mode:

        print("\nIniciando simulação noturna...")
        print("Painel solar desligado.")
        print(f"Duração: {NIGHT_HOURS} horas simuladas.")
        print(
            f"Tempo real: "
            f"{NIGHT_DURATION_SECONDS} segundos."
        )

    else:

        print("\nIniciando geração solar...")

        solar_panel.turn_on()

    start_time = time()

    last_consumption_update = start_time

    last_console_update = start_time

    # Guarda o resultado da última distribuição.
    result = {
        "attended": 0,
        "total_homes": len(homes),
        "energy_delivered": 0,
        "energy_remaining": battery_bank.get_available_energy(),
        "active_edges": set(),
        "paths": {}
    }

    try:

        while viewer.is_open():

            current_time = time()

            elapsed_real = current_time - start_time

            # =====================================
            # ATUALIZAÇÃO DO CONSUMO
            # =====================================

            if current_time - last_consumption_update >= 5:

                village.update_consumptions()

                last_consumption_update = current_time

            # =====================================
            # TEMPO DE SIMULAÇÃO
            # =====================================

            if night_mode:

                interval_seconds = NIGHT_STEP_SECONDS

                simulated_hours = (
                    elapsed_real
                    * NIGHT_HOURS
                    / NIGHT_DURATION_SECONDS
                )

            else:

                interval_seconds = 1

                simulated_hours = (
                    elapsed_real / 3600
                )

            # =====================================
            # DISTRIBUIÇÃO PELO GRAFO
            # =====================================

            result = distributor.distribute(
                interval_seconds=interval_seconds
            )

            # =====================================
            # ATUALIZAÇÃO VISUAL
            # =====================================

            viewer.update(
                result,
                battery_bank,
                mode,
                simulated_hours
            )

            # =====================================
            # INFORMAÇÕES NO TERMINAL
            # =====================================

            if current_time - last_console_update >= 2:

                print(
                    f"\rCasas atendidas: "
                    f"{result['attended']}/{result['total_homes']} | "
                    f"Bateria: "
                    f"{battery_bank.get_batteries_level():.2f}% | "
                    f"Energia: "
                    f"{battery_bank.get_available_energy():.2f} Wh",
                    end="",
                    flush=True
                )

                last_console_update = current_time

            # =====================================
            # ENCERRAMENTO DA SIMULAÇÃO NOTURNA
            # =====================================

            if night_mode:

                progress = min(
                    100,
                    (elapsed_real / NIGHT_DURATION_SECONDS) * 100
                )

                if elapsed_real >= NIGHT_DURATION_SECONDS:

                    print("\n\nAs 12 horas foram concluídas.")

                    break

            sleep(0.15)

    except KeyboardInterrupt:

        print("\n\nSimulação interrompida.")

    finally:

        # Garante que o painel seja desligado.
        solar_panel.turn_off()

        show_final_result(
            battery_bank,
            homes
        )

        if viewer.is_open():
            viewer.close()


if __name__ == "__main__":
    main()
