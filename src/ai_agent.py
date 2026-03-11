# ai_agent.py
"""
AI Agent (simulación) para AI-Augmented Data Analysis.
Permite seguir desarrollando el pipeline sin consumir tokens.
"""

def ask_ai_about_dataset(context, question):
    """
    Simula una respuesta de IA sobre el dataset.
    """
    # Podés personalizar los posibles análisis según tu dataset real
    simulated_response = """
Possible analyses:
1. Distribution of daily prices by neighborhood.
2. Relationship between ratings and price.
3. Impact of host experience on reviews.
4. Average occupancy vs. minimum nights.
5. Detect patterns in missing response rates.
"""
    return simulated_response