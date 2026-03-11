from src.ai_agent import ask_ai_about_dataset

def generate_report(context, questions):
    """
    Genera un reporte textual a partir de varias preguntas
    """
    report = "=== DATA ANALYSIS REPORT ===\n\n"

    for i, q in enumerate(questions, start=1):
        report += f"Q{i}: {q}\n"
        response = ask_ai_about_dataset(context, q)
        report += f"A{i}:\n{response}\n\n"

    return report