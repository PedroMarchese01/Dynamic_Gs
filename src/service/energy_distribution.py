
import networkx as nx


class EnergyDistribution:

    def __init__(
        self,
        battery_bank,
        village,
        edge_capacity_w=1000
    ):

        self.battery_bank = battery_bank
        self.village = village
        self.graph = village.graph

        self.edge_capacity_w = edge_capacity_w

        self.source_node = "ENERGY_SOURCE"

        homes = village.get_homes()

        if not homes:
            raise ValueError("A vila não possui casas.")

        # Cria a fonte de energia no grafo.
        self.graph.add_node(
            self.source_node,
            kind="source"
        )

        # Conecta a fonte à primeira casa.
        self.graph.add_edge(
            self.source_node,
            homes[0],
            capacity_w=edge_capacity_w
        )

        # Define a capacidade das conexões existentes.
        for u, v, data in self.graph.edges(data=True):

            data.setdefault(
                "capacity_w",
                edge_capacity_w
            )

    def distribute(self, interval_seconds=1):

        homes = self.village.get_homes()

        available_energy = (
            self.battery_bank.get_available_energy()
        )

        # Capacidade restante de cada conexão neste ciclo.
        residual_capacity = {}

        for u, v, data in self.graph.edges(data=True):

            capacity_w = data["capacity_w"]

            capacity_wh = (
                capacity_w * interval_seconds / 3600
            )

            residual_capacity[frozenset((u, v))] = capacity_wh

        # Calcula a demanda de cada casa.
        demands = []

        for home in homes:

            demand = home.get_energy_demand(
                interval_seconds
            )

            demand = max(0, demand)

            demands.append((home, demand))

        # Casas com menor demanda são priorizadas.
        demands.sort(key=lambda item: item[1])

        total_delivered = 0
        attended = 0

        allocations = {}
        active_edges = set()
        paths_used = {}

        # Grafo temporário para procurar caminhos disponíveis.
        residual_graph = nx.Graph()
        residual_graph.add_nodes_from(self.graph.nodes)

        # Distribuição.
        for home, demand in demands:

            allocations[home] = 0

            if demand <= 0:
                attended += 1
                continue

            if demand > available_energy:
                continue

            # Reconstrói os caminhos que ainda suportam
            # a demanda desta casa.
            residual_graph.clear()
            residual_graph.add_nodes_from(self.graph.nodes)

            for u, v in self.graph.edges():

                edge_key = frozenset((u, v))

                remaining_capacity = residual_capacity[
                    edge_key
                ]

                if remaining_capacity >= demand:
                    residual_graph.add_edge(u, v)

            # Procura o caminho mais curto até a casa.
            try:

                path = nx.shortest_path(
                    residual_graph,
                    source=self.source_node,
                    target=home
                )

            except nx.NetworkXNoPath:
                continue

            except nx.NodeNotFound:
                continue

            # A casa pode receber toda a demanda.
            allocations[home] = demand

            available_energy -= demand
            total_delivered += demand
            attended += 1

            paths_used[home] = path

            # Desconta a energia das conexões utilizadas.
            for i in range(len(path) - 1):

                u = path[i]
                v = path[i + 1]

                edge_key = frozenset((u, v))

                residual_capacity[edge_key] -= demand

                active_edges.add(edge_key)

        # Retira a energia do banco uma única vez.
        if total_delivered > 0:

            success = self.battery_bank.discharge(
                total_delivered
            )

            if not success:
                raise RuntimeError(
                    "Não foi possível retirar energia do banco."
                )

        # Atualiza as casas.
        for home, demand in demands:

            delivered = allocations[home]

            home.set_energy_received(delivered)

            # Mantém os dados disponíveis para a visualização.
            home.energy_demand = demand
            home.energy_received = delivered

            home.is_attended = (
                delivered >= demand - 0.0000001
            )

        return {
            "attended": attended,
            "total_homes": len(homes),
            "energy_delivered": total_delivered,
            "energy_remaining": (
                self.battery_bank.get_available_energy()
            ),
            "active_edges": active_edges,
            "paths": paths_used
        }
