from src.factory.village_factory import VillageFac
import networkx as nx
import matplotlib.pyplot as plt

# Criar vila
village = VillageFac()
village.append_number_of_home(10)

# Gerar grafo
graph = village.generate_graph()

# Converter casas em IDs numéricos
homes = list(graph.nodes())
home_ids = {home: f"Casa {i+1}" for i, home in enumerate(homes)}

# Criar layout visual
pos = nx.spring_layout(graph, seed=42, k=0.8)

# Desenhar grafo
plt.figure(figsize=(10, 8))

nx.draw_networkx(
    graph,
    pos,
    labels=home_ids,
    with_labels=True,
    node_color="skyblue",
    node_size=1800,
    font_size=10,
    font_weight="bold",
    edge_color="gray",
    width=2
)

plt.title("Mapa de conexões da Vila")
plt.axis("off")
plt.show()