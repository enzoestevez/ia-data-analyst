import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"

def plot_price_distribution(df):
    plt.figure(figsize=(8,5))
    plt.hist(df['Precio Diario'].dropna(), bins=30, color="#4C72B0", edgecolor="black")
    plt.title("Distribución de Precios Diarios", fontsize=14)
    plt.xlabel("Precio Diario", fontsize=12)
    plt.ylabel("Cantidad de Listings", fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "price_distribution.png"))
    plt.close()

def plot_rating_vs_price(df):
    plt.figure(figsize=(8,5))
    plt.scatter(df['Rating General'], df['Precio Diario'], alpha=0.6, color="#55A868")
    plt.title("Rating General vs Precio Diario", fontsize=14)
    plt.xlabel("Rating General", fontsize=12)
    plt.ylabel("Precio Diario", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "rating_vs_price.png"))
    plt.close()

def plot_missing_values(df):
    missing = df.isnull().sum()
    plt.figure(figsize=(12,5))
    missing.plot(kind='bar', color="#C44E52")
    plt.title("Valores Faltantes por Columna", fontsize=14)
    plt.ylabel("Cantidad de Missing Values", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "missing_values.png"))
    plt.close()