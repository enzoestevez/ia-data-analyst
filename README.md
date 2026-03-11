# AI-Augmented Data Analysis - Airbnb Dataset

Proyecto de portfolio que demuestra un **pipeline completo de análisis de datos potenciado con IA**, con reportes automáticos y visualizaciones profesionales.  
El objetivo es simular cómo un Analista de Datos puede extraer insights de un dataset real, generar reportes y visualizar resultados de forma profesional.


## 🔹 Estructura del proyecto
    ai-data-analyst/
    │
    ├─ data/ # Dataset original (airbnb.csv)
    ├─ outputs/ # Gráficos y reportes generados automáticamente
    ├─ src/ # Módulos de Python
    │ ├─ data_loader.py
    │ ├─ ai_context_builder.py
    │ ├─ ai_agent.py
    │ ├─ report_generator.py
    │ └─ visualizations.py
    ├─ main.py # Script principal para ejecutar todo el pipeline
    └─ README.md # Este archivo


## 🔹 Instalación y ejecución

1. Crear y activar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# o
source venv/bin/activate # Mac/Linux
```
2. instalar dependencias

```bash
pip install pandas
```
3. Ejecutar el pipeline completo:

```bash
    python main.py
```

## Qué genera el proyecto

- Dataset Overview: filas, columnas, tipos de datos y missing values.
- AI Dataset Context: descripción resumida del dataset para IA.
- Reporte automático: insights simulados de IA sobre el dataset.
- Visualizaciones profesionales:
 - price_distribution.png → Distribución de precios diarios.
 - rating_vs_price.png → Relación entre Rating General y Precio Diario.
 - missing_values.png → Valores faltantes por columna.

## Próximos pasos / mejoras

    1. Reemplazar el AI Agent simulado por IA real (OpenAI GPT) cuando haya acceso a tokens o plan.
    2. Mejorar gráficos con Plotly para interactividad.
    3. Exportar reportes a PDF para entregar análisis profesional completo.
    4. Agregar más análisis automatizados basados en correlaciones o segmentaciones.

🔹 Tecnologías utilizadas

    - Python 3
    - Pandas (procesamiento de datos)
    - Matplotlib (visualización)
    - AI-simulación para insights (modular para reemplazar con IA real)

## Sobre el autor

    Enzo Estévez – Estudiante de Analista Universitario en Ciencia de Datos, UNLU.
    Portfolio: https://enzoestevez.com
    GitHub: https://github.com/enzoestevez
    linkedin: https://www.linkedin.com/in/enzoestevez/