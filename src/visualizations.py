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


def plot_price_boxplot(df):

    plt.figure(figsize=(8,5))

    plt.boxplot(df['Precio Diario'].dropna(), vert=False)

    plt.title("Distribución de Precios (Boxplot)", fontsize=14)
    plt.xlabel("Precio Diario")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "price_boxplot.png"))

    plt.close()


def plot_top_neighborhoods(df):

    if "Barrio" not in df.columns:
        return

    avg_prices = df.groupby("Barrio")["Precio Diario"].mean().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,6))

    avg_prices.plot(kind="bar", color="#8172B2")

    plt.title("Top 10 Barrios por Precio Promedio", fontsize=14)
    plt.xlabel("Barrio")
    plt.ylabel("Precio Promedio")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "top_neighborhoods_price.png"))

    plt.close()


def plot_correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=['number'])

    corr = numeric_df.corr()

    plt.figure(figsize=(8,6))

    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")

    plt.colorbar()

    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))

    plt.close()