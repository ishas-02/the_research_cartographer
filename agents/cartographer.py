from config.settings import model

def agent_cartographer(text):
    prompt = f"""
    You are an expert Research Architect.

    Extract a structured KNOWLEDGE GRAPH from this paper.
    STRICT FORMAT (do not deviate):

    * [Node A] -> RELATION -> [Node B]

    Identify:
    - Methods
    - Datasets
    - Results
    - Key relationships

    TEXT:
    {text[:30000]}
    """
    response = model.generate_content(prompt)
    return response.text
