import streamlit as st
import os
import matplotlib.pyplot as plt
import re

from tools.pdf_parser import parse_pdf

# STATIC graph (returns a Matplotlib Figure or None)
from tools.graph_visualizer import draw_graph as draw_static_graph  

# INTERACTIVE graph (returns HTML path or None)
from tools.graph_interactive import draw_graph as draw_interactive_graph

from agents.cartographer import agent_cartographer
from agents.navigator import agent_navigator


st.set_page_config(page_title="Research Paper Navigator", layout="wide")


# ===============================================================
# 🔍 Extract top Methods / Datasets / Results (Cards)
# ===============================================================
def extract_top_cards(knowledge_text: str):
    triples = re.findall(r"\[(.*?)\]\s*->\s*(.*?)\s*->\s*\[(.*?)\]", knowledge_text)

    methods, datasets, results = set(), set(), set()

    for src, rel, tgt in triples:
        s, t, r = src.lower(), tgt.lower(), rel.lower()

        # METHODS
        if any(k in s for k in ["model", "framework", "method", "cnn", "transformer", "yolov", "lstm"]):
            methods.add(src)
        if any(k in t for k in ["model", "framework", "method", "cnn", "transformer", "yolov", "lstm"]):
            methods.add(tgt)

        # DATASETS
        if any(k in s for k in ["dataset", "data", "stereo", "kitti", "image pair"]):
            datasets.add(src)
        if any(k in t for k in ["dataset", "data", "stereo", "kitti", "image pair"]):
            datasets.add(tgt)

        # RESULTS
        if any(k in r for k in ["achieved", "accuracy", "score", "result", "evaluated", "performance"]):
            results.add(tgt)

    return list(methods), list(datasets), list(results)


# ===============================================================
# 🔧 Helper: run full pipeline for one paper
# ===============================================================
def process_paper(uploaded_file):
    """Run parse → cartographer → cards for a single PDF."""
    # Save temp file
    temp_path = "uploaded_temp.pdf"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    raw_text = parse_pdf(temp_path)
    knowledge_map = agent_cartographer(raw_text)
    methods, datasets, results = extract_top_cards(knowledge_map)

    # Static graph
    fig = draw_static_graph(knowledge_map)

    # Interactive graph
    html_path = draw_interactive_graph(knowledge_map)

    return {
        "name": uploaded_file.name,
        "raw_text": raw_text,
        "knowledge_map": knowledge_map,
        "methods": methods,
        "datasets": datasets,
        "results": results,
        "fig": fig,
        "html_path": html_path,
    }


# ===============================================================
# 📌 UI HEADER
# ===============================================================
st.title("📚 Research Paper Navigator")
st.write(
    "Upload one or more research papers as PDF. "
    "You can inspect a single paper, or compare two papers side-by-side."
)


# ===============================================================
# 📂 PDF UPLOAD (NOW MULTI-FILE)
# ===============================================================
uploaded_files = st.file_uploader(
    "Upload Research Paper PDF(s)", type=["pdf"], accept_multiple_files=True
)

if not uploaded_files:
    st.info("Upload 1 PDF for single analysis, or 2 PDFs for side-by-side comparison.")
else:
    # ===========================================================
    # SINGLE-PAPER MODE
    # ===========================================================
    if len(uploaded_files) == 1:
        paper = process_paper(uploaded_files[0])

        st.success(f"📄 Loaded: {paper['name']}")

        # TEXT PREVIEW
        st.subheader("📝 Extracting Text...")
        st.text_area(
            "Text Preview (First 2000 characters):",
            paper["raw_text"][:2000],
            height=200,
        )

        # KNOWLEDGE MAP
        st.subheader("🧠 Generating Knowledge Map...")
        st.text_area(
            "Agent-Extracted Graph Triples",
            paper["knowledge_map"],
            height=230,
        )

        # CARDS
        st.subheader("📊 Key Insights Overview")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("### ⭐ Top Methods")
            for m in paper["methods"][:6]:
                st.success(m)

        with c2:
            st.markdown("### 📂 Top Datasets")
            for d in paper["datasets"][:6]:
                st.info(d)

        with c3:
            st.markdown("### 🏆 Top Results")
            for r in paper["results"][:6]:
                st.warning(r)

        # STATIC GRAPH
        st.subheader("📌 Static Knowledge Graph Visualization")
        if paper["fig"] is not None:
            st.pyplot(paper["fig"])
        else:
            st.warning("⚠️ No valid graph relationships found.")

        # INTERACTIVE GRAPH
        st.subheader("🌐 Interactive Knowledge Graph (Zoom & Drag)")
        from streamlit.components.v1 import html

        if paper["html_path"] and os.path.exists(paper["html_path"]):
            with open(paper["html_path"], "r", encoding="utf-8") as f:
                html_data = f.read()
            html(html_data, height=700)
        else:
            st.error("Interactive graph could not be generated.")

        # Q&A
        st.subheader("❓ Ask a Question About the Paper")
        question = st.text_input("Enter your question:")

        if st.button("Get Answer"):
            answer = agent_navigator(paper["knowledge_map"], question)
            st.markdown(f"### 💡 Answer:\n{answer}")

    # ===========================================================
    # TWO-PAPER COMPARISON MODE
    # ===========================================================
    else:
        st.success(f"📄 Loaded {len(uploaded_files)} PDFs. Comparing first two.")

        paper_left = process_paper(uploaded_files[0])
        paper_right = process_paper(uploaded_files[1])

        st.subheader("📊 Side-by-Side Comparison")

        col_left, col_right = st.columns(2)

        # ---------- LEFT PAPER ----------
        with col_left:
            st.markdown(f"## 📄 Paper A: *{paper_left['name']}*")

            st.markdown("### ⭐ Top Methods")
            for m in paper_left["methods"][:6]:
                st.success(m)

            st.markdown("### 📂 Top Datasets")
            for d in paper_left["datasets"][:6]:
                st.info(d)

            st.markdown("### 🏆 Top Results")
            for r in paper_left["results"][:6]:
                st.warning(r)

            st.markdown("### 📌 Static Graph (Paper A)")
            if paper_left["fig"] is not None:
                st.pyplot(paper_left["fig"])
            else:
                st.write("No graph for this paper.")

        # ---------- RIGHT PAPER ----------
        with col_right:
            st.markdown(f"## 📄 Paper B: *{paper_right['name']}*")

            st.markdown("### ⭐ Top Methods")
            for m in paper_right["methods"][:6]:
                st.success(m)

            st.markdown("### 📂 Top Datasets")
            for d in paper_right["datasets"][:6]:
                st.info(d)

            st.markdown("### 🏆 Top Results")
            for r in paper_right["results"][:6]:
                st.warning(r)

            st.markdown("### 📌 Static Graph (Paper B)")
            if paper_right["fig"] is not None:
                st.pyplot(paper_right["fig"])
            else:
                st.write("No graph for this paper.")

        # ---------- OPTIONAL: COMPARISON NOTES ----------
        st.subheader("🧾 Comparison Notes")
        st.write(
            "Use this space to note key differences between the two papers "
            "(methods, datasets, results, novelty, limitations, etc.)."
        )
        st.text_area("Your comparison notes:", height=150)

        # ---------- SIMPLE COMPARISON Q&A ----------
        st.subheader("❓ Ask a Comparison Question")
        compare_question = st.text_input(
            "Ask something like: 'How do the methods differ between Paper A and Paper B?'"
        )

        if st.button("Get Comparison Answer"):
            # Concatenate both knowledge maps with tags
            combined_map = (
                f"--- PAPER A ({paper_left['name']}) ---\n"
                f"{paper_left['knowledge_map']}\n\n"
                f"--- PAPER B ({paper_right['name']}) ---\n"
                f"{paper_right['knowledge_map']}"
            )
            answer = agent_navigator(combined_map, compare_question)
            st.markdown(f"### 💡 Comparison Answer:\n{answer}")

