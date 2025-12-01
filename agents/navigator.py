from config.settings import model

def agent_navigator(knowledge_graph, question):
    prompt = f"""
    You are a Research Navigator.

    Use the KNOWLEDGE GRAPH to answer clearly.

    KNOWLEDGE MAP:
    {knowledge_graph}

    QUESTION:
    {question}
    """
    response = model.generate_content(prompt)
    return response.text
