from pyvis.network import Network
import re
import networkx as nx

def draw_graph(graph_text, output_html="interactive_graph.html"):
    """
    Builds an interactive PyVis graph from agent-generated triples.
    Returns path to HTML file for Streamlit iframe display.
    """

    triples = re.findall(r"\[(.*?)\]\s*->\s*(.*?)\s*->\s*\[(.*?)\]", graph_text)
    if not triples:
        return None

    G = nx.DiGraph()
    
    for src, rel, tgt in triples:
        G.add_node(src.strip())
        G.add_node(tgt.strip())
        G.add_edge(src.strip(), tgt.strip(), label=rel.strip())

    net = Network(
        height="700px",
        width="100%",
        directed=True,
        bgcolor="#1e1e1e",
        font_color="white"
    )

    net.from_nx(G)

    net.repulsion(
        node_distance=180,
        central_gravity=0.2,
        spring_length=180,
        spring_strength=0.05,
        damping=0.9
    )

    for u, v, data in G.edges(data=True):
        net.add_edge(u, v, title=data.get("label", ""), label=data.get("label", ""))

    net.save_graph(output_html)
    return output_html
