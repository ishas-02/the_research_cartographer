from orchestrator.research_navigator import run_research_navigator

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Research Paper Navigator - PDF → Knowledge Graph → Q&A")
    parser.add_argument("--pdf", type=str, required=True, help="Folder containing the PDF")
    parser.add_argument("--question", type=str, required=True, help="Your research question")
    args = parser.parse_args()

    run_research_navigator(args.pdf, args.question)
