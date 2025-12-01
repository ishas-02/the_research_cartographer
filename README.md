🌌 The Research Cartographer
Mapping the Hidden Architecture of Scientific Papers
<p align="center"> <img src="assets/banner.png" width="75%"> </p>
🚀 Overview

The Research Cartographer is an AI-powered multi-agent system that transforms dense academic PDFs into structured knowledge maps, insight cards, comparisons, and interactive visual graphs.

It reads research papers like an expert would — extracting key entities, mapping relationships, and answering questions — turning the literature review process into an interactive exploration.

This tool is ideal for:

Researchers

Students

Machine learning engineers

Anyone doing literature reviews or comparative studies

✨ Features
🔍 1. PDF Understanding

Extracts clean text from academic papers using a robust parsing pipeline.

🧠 2. Agent-Based Triple Extraction

Uses an LLM to produce structured relationships:

[Method] -> USES -> [Dataset]
[Model] -> ACHIEVES -> [Result]

📊 3. Insight Cards

Automatically identifies:

⭐ Top Methods

📂 Top Datasets

🏆 Top Results

🎨 4. Static Knowledge Graph (NetworkX)

Color-coded graph showing the structure of the research:

Blue → Methods

Green → Datasets

Yellow → Results

Grey → Other concepts

🌐 5. Interactive Graph (PyVis)

A draggable, zoomable, hover-enabled visualization for exploring the paper as a semantic network.

⁉️ 6. Research Q&A Agent

Ask questions like:

“What is the main contribution?”

“How does this paper differ from Paper B?”

“What datasets were used?”

The Navigator agent answers using the extracted knowledge graph.

⚔️ 7. Side-by-Side Paper Comparison

Supports two-paper mode:

Extracts both graphs

Summarizes both papers

Highlights differences in methods, datasets, and results

Provides comparative insights

🧭 System Architecture
📄 PDF → 🧹 Text Extractor
       → 🧠 Cartographer Agent (Triples)
       → 🎯 Insight Classifier
       → 🎨 Static Graph Builder
       → 🌐 Interactive Graph Builder
       → ❓ Navigator Agent (Q&A)
       → ⚔️ Paper Comparison Engine

📂 Project Structure
The-Research-Cartographer/
│
├── app.py                      # Streamlit dashboard
├── main.py                     # CLI runner
├── environment.yml             # Conda environment setup
├── README.md                   # Documentation
│
├── agents/
│   ├── cartographer.py         # Triple extractor agent
│   └── navigator.py            # Q&A agent
│
├── tools/
│   ├── pdf_parser.py           # PDF -> text
│   ├── graph_visualizer.py     # Static graph
│   └── graph_interactive.py    # Interactive PyVis graph
│
├── assets/                     # Images, banner, screenshots
│
└── sample_papers/              # Example PDFs (optional)

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/research-cartographer.git
cd research-cartographer

2️⃣ Create the Conda environment
conda env create -f environment.yml
conda activate my_cartographer

3️⃣ Set up your Google API key (DO NOT HARD-CODE IT)

Create a local environment variable:

export GOOGLE_API_KEY="your_api_key_here"


Or in Windows PowerShell:

setx GOOGLE_API_KEY "your_api_key_here"

▶️ Running the Streamlit App
streamlit run app.py


App will open at:

http://localhost:8501


Upload a research paper → view graphs → explore → compare → ask questions.

🧪 Example Output
🔹 Insight Cards
Top Methods:
- Stereo Vision Depth Estimation
- CNN Behavior Classifier
- LSTM Risk Score Module

🔹 Knowledge Triples
[Stereo camera] -> ESTIMATES -> [object depth]
[CNN classifier] -> CLASSIFIES -> [driver behavior]

🎨 Static Graph

(Add a screenshot to assets/static_graph_sample.png)

🌐 Interactive Graph

(Add a screenshot to assets/interactive_graph_sample.png)

⚔️ Paper Comparison

Upload two PDFs to automatically generate:

Two knowledge graphs

Two sets of insight cards

Automatic difference analysis

Comparative Q&A

This mode is extremely helpful for literature reviews.

🛠️ Tech Stack
Component	Technology
LLM Engine	Gemini 2.0 Flash
PDF Parsing	PyPDF
Static Graphs	NetworkX + Matplotlib
Interactive Graphs	PyVis
Web UI	Streamlit
Language	Python 3
🚧 Limitations

Multi-column PDFs may extract text imperfectly

Triple extraction depends on LLM consistency

Node classification uses heuristic keyword matching

Long PDFs are truncated for efficiency

🌱 Future Enhancements

Full long-document chunking workflow

Automatic literature review generation

Extraction of figures, tables, equations

Multi-paper clustering and similarity analysis

Citation graph extraction

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you'd like to improve.

⭐ Support the Project

If you found this useful:

⭐ Star the repo

🔁 Share with other researchers

💬 Suggest improvements