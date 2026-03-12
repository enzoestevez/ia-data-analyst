# main.py
import os
import pandas as pd
from src.data_loader import load_dataset, get_dataset_overview
from src.ai_context_builder import build_dataset_context
from src.report_generator import generate_report
from src.visualizations import (
    plot_price_distribution,
    plot_rating_vs_price,
    plot_missing_values,
    plot_price_boxplot,
    plot_top_neighborhoods,
    plot_correlation_heatmap
)

def main():
    # 1️⃣ Crear carpeta outputs si no existe
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    # 2️⃣ Cargar dataset
    dataset_path = "data/airbnb.csv"
    print(f"Loading dataset from {dataset_path}...")
    df = load_dataset(dataset_path)

    # 3️⃣ Convertir columnas importantes a numérico
    df['Precio Diario'] = pd.to_numeric(df['Precio Diario'], errors='coerce')
    df['Rating General'] = pd.to_numeric(df['Rating General'], errors='coerce')

    # 4️⃣ Generar overview del dataset
    overview = get_dataset_overview(df)
    print("\nDATASET OVERVIEW")
    print("-------------------")
    print(f"Rows: {overview['rows']}")
    print(f"Columns: {overview['columns']}")
    print("\nMissing Values:")
    for col, val in overview["missing_values"].items():
        print(f"{col}: {val}")

    # 5️⃣ Construir contexto para IA
    context = build_dataset_context(overview)
    print("\nAI DATASET CONTEXT")
    print("-------------------")
    print(context)

    # 6️⃣ Definir preguntas automáticas
    questions = [
        "What interesting insights could we explore from this Airbnb dataset?",
        "Which columns have the most missing values and how could we handle them?",
        "Suggest visualizations that could be useful for this dataset"
    ]

    # 7️⃣ Generar reporte automático
    report = generate_report(context, questions)
    print("\nAUTOMATIC REPORT")
    print("-------------------")
    print(report)

    # 8️⃣ Filtrar filas válidas para gráficas
    df_plot = df.dropna(subset=['Precio Diario', 'Rating General'])

    # 9️⃣ Generar visualizaciones profesionales
    plot_price_distribution(df_plot)
    plot_rating_vs_price(df_plot)
    plot_missing_values(df_plot)

    plot_price_boxplot(df_plot)
    plot_top_neighborhoods(df_plot)
    plot_correlation_heatmap(df_plot)

    print("\nVisualizations saved in 'outputs/'")

if __name__ == "__main__":
    main()