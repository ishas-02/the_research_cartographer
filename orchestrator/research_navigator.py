import os
from tools.pdf_parser import parse_pdf
from tools.graph_visualizer import draw_graph
from agents.cartographer import agent_cartographer
from agents.navigator import agent_navigator

def run_research_navigator(pdf_folder, question):
    print("\n🚀 Starting Research Paper Navigator...\n")

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]
    if not pdf_files:
        raise FileNotFoundError("❌ No PDF found in the folder.")

    pdf_path = os.path.join(pdf_folder, pdf_files[0])
    print(f"📂 Loaded PDF: {pdf_files[0]}")

    # 1. Extract raw text
    raw_text = parse_pdf(pdf_path)

    # 2. Build knowledge graph
    knowledge_map = agent_cartographer(raw_text)

    # 3. Visualize graph
    draw_graph(knowledge_map)

    # 4. Answer custom question
    final_answer = agent_navigator(knowledge_map, question)
    print("\n💡 ANSWER:\n", final_answer)

    return final_answer
