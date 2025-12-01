Absolutely — here is a **perfectly formatted, GitHub-ready `README.md`** that you can **copy–paste exactly as is**.
It includes **Markdown headings, centered banner placeholder, tables, code blocks, spacing, and section formatting**.

👉 **You can paste this directly into GitHub — it will render beautifully.**

---

# 🌌 **The Research Cartographer**

### *Mapping the Hidden Architecture of Scientific Papers*

<p align="center">
  <img src="assets/banner.png" width="75%">
</p>

---

## 🚀 Overview

**The Research Cartographer** is an AI-powered multi-agent system that transforms dense academic PDFs into **structured knowledge maps**, **insight cards**, **comparisons**, and **interactive visual graphs**.

Instead of manually deciphering methods, datasets, and results, this tool acts as a **research co-pilot** that:

* Extracts key concepts and relationships
* Builds semantic knowledge graphs
* Highlights top methods, datasets, and results
* Enables side-by-side comparison of multiple papers
* Answers questions using a Q&A agent

It makes literature review **visual, interactive, and insightful**.

---

## ✨ Features

### 🔍 **1. PDF Understanding**

Extracts structured text from research papers using PDF parsing tools.

### 🧠 **2. Triple-Based Knowledge Extraction**

Uses an LLM-powered agent to output structured relationships like:

```
[Method] -> USES -> [Dataset]
[Model] -> ACHIEVES -> [Result]
```

### ⭐ **3. Insight Cards**

Automatically identifies and displays:

* Top Methods
* Top Datasets
* Top Results

### 🎨 **4. Static Knowledge Graph**

Uses NetworkX + Matplotlib to build a color-coded graph:

* 🔵 Methods
* 🟢 Datasets
* 🟡 Results
* ⚪ Other concepts

### 🌐 **5. Interactive Graph**

A PyVis-based graph where users can:

* Drag nodes
* Zoom & pan
* Hover edges to see relationships

### ❓ **6. Research Q&A**

Ask the agent:

* “What is the main contribution?”
* “What datasets were used?”
* “What differentiates this from another paper?”

### ⚔️ **7. Side-by-Side Paper Comparison**

Upload two PDFs → the system automatically:

* Extracts graphs
* Summarizes insights
* Compares methods, datasets, and results
* Shows differences

---

## 🧭 System Architecture

```
📄 PDF → 🧹 Text Extractor
       → 🧠 Cartographer Agent (Triples)
       → 🎯 Insight Classifier
       → 🎨 Static Graph Builder
       → 🌐 Interactive Graph Builder
       → ❓ Navigator Q&A Agent
       → ⚔️ Comparison Engine (multi-paper mode)
```

---

## 📂 Project Structure

```
The-Research-Cartographer/
│
├── app.py                      # Streamlit UI Dashboard
├── main.py                     # CLI Runner (optional)
├── environment.yml             # Conda Environment
├── README.md                   # Project Documentation
│
├── agents/
│   ├── cartographer.py         # Knowledge Triple Extractor
│   └── navigator.py            # Question-Answering Agent
│
├── tools/
│   ├── pdf_parser.py           # PDF Text Extractor
│   ├── graph_visualizer.py     # Static Graph (NetworkX)
│   └── graph_interactive.py    # Interactive Graph (PyVis)
│
├── assets/
│   ├── banner.png              # Repo Banner
│   ├── static_graph_sample.png # Example Output
│   └── interactive_graph_sample.png
│
└── sample_papers/              # Optional sample PDFs
```

---

## ⚙️ Installation

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/your-username/research-cartographer.git
cd research-cartographer
```

### **2️⃣ Create the Conda environment**

```bash
conda env create -f environment.yml
conda activate my_cartographer
```

### **3️⃣ Add your Gemini API key securely**

**DO NOT hard-code your key in the code.**

Use environment variables:

Mac/Linux:

```bash
export GOOGLE_API_KEY="your_key_here"
```

Windows PowerShell:

```powershell
setx GOOGLE_API_KEY "your_key_here"
```

---

## ▶️ Running the Streamlit App

```bash
streamlit run app.py
```

This opens the dashboard at:

👉 **[http://localhost:8501](http://localhost:8501)**

Upload a PDF → see knowledge graphs → ask questions → compare papers.

---

## 🧪 Example Output

### ⭐ **Insight Cards**

```
Top Methods:
- Stereo Vision Depth Estimation
- CNN-Based Driver Behavior Recognition
- LSTM Risk Scoring
```

### 🧠 **Knowledge Triples**

```
[Stereo Camera] -> ESTIMATES -> [Object Depth]
[CNN Classifier] -> CLASSIFIES -> [Driver Behavior]
```

### 🎨 **Static Graph Example**

<p align="center">
  <img src="assets/static_graph_sample.png" width="70%">
</p>

### 🌐 **Interactive Graph Example**

<p align="center">
  <img src="assets/interactive_graph_sample.png" width="70%">
</p>

---

## ⚔️ Side-by-Side Comparison

The system automatically generates:

* Two knowledge maps
* Two sets of insight cards
* Overlap & difference analysis
* Comparative Q&A

Perfect for literature reviews and benchmarking.

---

## 🛠️ Tech Stack

| Component          | Technology            |
| ------------------ | --------------------- |
| LLM Engine         | Gemini 2.0 Flash      |
| PDF Parsing        | PyPDF                 |
| Static Graphs      | NetworkX + Matplotlib |
| Interactive Graphs | PyVis                 |
| Interface          | Streamlit             |
| Language           | Python 3              |

---

## 🚧 Limitations

* Multi-column PDFs may not extract perfectly
* Triple extraction depends on LLM consistency
* Keyword-based classification may mislabel some nodes
* Very long PDFs are truncated for speed

---

## 🌱 Future Improvements

* Chunked long-document processing
* Extracting tables, equations, and figures
* Automatic literature review generation
* Semantic clustering of research papers
* Citation graph extraction

---

## 🤝 Contributing

Contributions are welcome!
Just fork the repo, create a branch, and submit a PR.

---

## ⭐ Support the Project

If you find this useful, please:

* ⭐ Star the repository
* 🔁 Share it with your peers
* 🐛 Report bugs
* 💡 Suggest new features

---

