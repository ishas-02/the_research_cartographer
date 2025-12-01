# # import re
# # import networkx as nx
# # import matplotlib.pyplot as plt

# # def draw_graph(graph_text):
# #     """
# #     Converts the agent-generated text into a real visual graph.
# #     """
# #     print("🎨 Rendering Knowledge Graph...")

# #     pattern = r"\[(.*?)\]\s*->\s*(.*?)\s*->\s*\[(.*?)\]"
# #     relationships = re.findall(pattern, graph_text)

# #     if not relationships:
# #         print("⚠️ No valid relationships found.")
# #         return

# #     G = nx.DiGraph()

# #     for source, relation, target in relationships:
# #         G.add_edge(source.strip(), target.strip(), label=relation.strip())

# #     plt.figure(figsize=(14, 10))
# #     pos = nx.spring_layout(G, seed=42, k=0.6)

# #     nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightblue')
# #     nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
# #     nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', width=2)

# #     labels = nx.get_edge_attributes(G, 'label')
# #     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

# #     plt.title("Research Paper Knowledge Graph", fontsize=16)
# #     plt.axis("off")
# #     plt.show()

# import re
# import networkx as nx
# import matplotlib.pyplot as plt

# def draw_graph(graph_text):
#     """
#     Converts the agent-generated text into a real visual graph (static).
#     """
#     print("🎨 Rendering Static Knowledge Graph...")

#     pattern = r"\[(.*?)\]\s*->\s*(.*?)\s*->\s*\[(.*?)\]"
#     relationships = re.findall(pattern, graph_text)

#     if not relationships:
#         print("⚠️ No valid relationships found.")
#         return

#     G = nx.DiGraph()

#     for source, relation, target in relationships:
#         G.add_edge(source.strip(), target.strip(), label=relation.strip())

#     plt.figure(figsize=(14, 10))
#     pos = nx.spring_layout(G, seed=42, k=0.6)

#     nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightblue')
#     nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
#     nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', width=2)

#     labels = nx.get_edge_attributes(G, 'label')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

#     plt.title("Research Paper Knowledge Graph", fontsize=16)
#     plt.axis("off")

import re
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph_text):
    """
    Converts the agent-generated text into a real visual graph (static)
    and returns a Matplotlib figure.
    """

    pattern = r"\[(.*?)\]\s*->\s*(.*?)\s*->\s*\[(.*?)\]"
    relationships = re.findall(pattern, graph_text)

    if not relationships:
        print("⚠️ No valid relationships found.")
        return None

    G = nx.DiGraph()

    for source, relation, target in relationships:
        G.add_edge(source.strip(), target.strip(), label=relation.strip())

    fig = plt.figure(figsize=(14, 10))   # 🎯 Create figure object
    pos = nx.spring_layout(G, seed=42, k=0.6)

    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
    nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='-|>', width=2)

    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red')

    plt.title("Research Paper Knowledge Graph", fontsize=16)
    plt.axis("off")

    return fig   # ⭐ MOST IMPORTANT LINE
