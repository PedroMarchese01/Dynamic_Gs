import matplotlib.pyplot as plt
import networkx as nx


class LiveVillageView:

    def __init__(self, graph, homes, source_node):

        self.graph = graph
        self.homes = homes
        self.source_node = source_node

        self.positions = nx.spring_layout(
            graph,
            seed=42,
            k=0.8
        )

        self.nodes = list(graph.nodes)
        self.edges = list(graph.edges)

        self.figure, (self.ax, self.info_ax) = (
            plt.subplots(
                1,
                2,
                figsize=(15, 9),
                gridspec_kw={"width_ratios": [1.5, 1]}
            )
        )

        self.figure.canvas.manager.set_window_title(
            "Monitoramento da Vila"
        )

        self.ax.set_title("REDE ELÉTRICA")
        self.ax.axis("off")

        # Desenha as conexões apenas uma vez.
        self.edge_collection = nx.draw_networkx_edges(
            graph,
            self.positions,
            ax=self.ax,
            edgelist=self.edges,
            edge_color="#888888",
            width=1.5,
            alpha=0.8
        )

        # Desenha os nós apenas uma vez.
        self.node_collection = nx.draw_networkx_nodes(
            graph,
            self.positions,
            ax=self.ax,
            nodelist=self.nodes,
            node_color="#e74c3c",
            node_size=450,
            edgecolors="black"
        )

        labels = {
            home: f"H{i + 1}"
            for i, home in enumerate(homes)
        }

        labels[source_node] = "FONTE"

        nx.draw_networkx_labels(
            graph,
            self.positions,
            labels=labels,
            ax=self.ax,
            font_size=7,
            font_weight="bold"
        )

        self.info_ax.axis("off")

        self.info_ax.set_title(
            "MONITORAMENTO ENERGÉTICO"
        )

        # Texto atualizado sem criar novos objetos.
        self.info_text = self.info_ax.text(
            0.01,
            0.98,
            "",
            verticalalignment="top",
            fontsize=8,
            fontfamily="monospace"
        )

        self.figure.tight_layout()

        plt.ion()
        plt.show(block=False)
        plt.pause(0.1)

    def update(self, result, battery_bank, mode, elapsed):

        # =========================
        # CORES DAS CASAS
        # =========================

        colors = []

        for node in self.nodes:

            if node == self.source_node:
                colors.append("#3498db")
                continue

            attended = getattr(
                node,
                "is_attended",
                False
            )

            if attended:
                colors.append("#2ecc71")
            else:
                colors.append("#e74c3c")

        self.node_collection.set_facecolors(colors)

        # =========================
        # CONEXÕES UTILIZADAS
        # =========================

        active_edges = result.get(
            "active_edges",
            set()
        )

        edge_colors = []

        for u, v in self.edges:

            if frozenset((u, v)) in active_edges:
                edge_colors.append("#2ecc71")
            else:
                edge_colors.append("#888888")

        self.edge_collection.set_color(edge_colors)

        # =========================
        # INFORMAÇÕES
        # =========================

        lines = []

        lines.append(f"MODO: {mode}")
        lines.append(f"TEMPO: {elapsed:.2f} horas")
        lines.append("")

        lines.append(
            f"CASAS ATENDIDAS: "
            f"{result['attended']}/{result['total_homes']}"
        )

        lines.append(
            f"BATERIA: "
            f"{battery_bank.get_batteries_level():.2f}%"
        )

        lines.append(
            f"ENERGIA: "
            f"{battery_bank.get_available_energy():.2f} Wh"
        )

        lines.append(
            f"ENTREGUE: "
            f"{result['energy_delivered']:.4f} Wh"
        )

        lines.append("")
        lines.append("DETALHAMENTO DAS CASAS")
        lines.append("-" * 42)

        for i, home in enumerate(self.homes):

            demand = getattr(
                home,
                "energy_demand",
                0
            )

            received = getattr(
                home,
                "energy_received",
                0
            )

            if home.is_attended:
                status = "OK"
            else:
                status = "SEM ENERGIA"

            lines.append(
                f"H{i + 1:02} | {status:<10} "
                f"| {received:.4f}/{demand:.4f} Wh"
            )

        self.info_text.set_text(
            "\n".join(lines)
        )

        # Atualiza os objetos existentes.
        self.figure.canvas.draw_idle()
        self.figure.canvas.flush_events()

    def is_open(self):
        return plt.fignum_exists(
            self.figure.number
        )

    def close(self):
        plt.close(self.figure)
