# AI-Augmented Data Analysis – Airbnb Dataset

Portfolio project demonstrating a **complete AI-augmented data analysis pipeline** using Python.
The project loads a real Airbnb dataset, performs **Exploratory Data Analysis (EDA)**, generates **professional visualizations**, and produces **AI-generated insights** using the OpenAI API.

The goal is to simulate how a **Data Analyst can combine traditional data analysis with AI tools** to generate insights and reports automatically.

---

# Project Structure

```
ai-data-analyst/
│
├── data/
│   └── airbnb.csv                 # Original dataset
│
├── outputs/                       # Generated charts and reports
│
├── src/
│   ├── data_loader.py             # Dataset loading and overview
│   ├── ai_context_builder.py      # Converts dataset overview into AI-readable context
│   ├── ai_agent.py                # OpenAI-powered analysis agent
│   ├── report_generator.py        # Automatic report generation
│   └── visualizations.py          # Professional data visualizations
│
├── main.py                        # Main pipeline execution script
│
└── README.md                      # Project documentation
```

---

# Features

This project includes a **full analysis workflow**:

### Data Processing

* Dataset loading
* Dataset overview generation
* Missing values detection
* Data type inspection

### AI-Augmented Analysis

* Dataset context builder
* AI-powered analytical insights using OpenAI
* Automated question-based reporting

### Exploratory Data Analysis (EDA)

The pipeline automatically generates professional visualizations:

1. Price Distribution
2. Rating vs Price Relationship
3. Missing Values per Column
4. Price Distribution Boxplot (Outlier Detection)
5. Top Neighborhoods by Average Price
6. Correlation Heatmap of Numeric Variables

These graphs simulate the type of analysis a **data analyst would perform when exploring a dataset for the first time.**

---

# Installation

Clone the repository:

```bash
git clone https://github.com/enzoestevez/ai-data-analyst.git
cd ai-data-analyst
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install pandas matplotlib openai
```

---

# OpenAI API Setup

This project integrates **OpenAI to generate analytical insights**.

For security reasons, the API key is **not included in the repository**.

Set your environment variable before running the project.

Windows:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

Mac/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Restart the terminal after setting the variable.

---

# Running the Project

Execute the full analysis pipeline:

```bash
python main.py
```

The pipeline will:

1. Load the dataset
2. Generate a dataset overview
3. Build an AI-readable dataset context
4. Ask the AI analytical questions
5. Generate an automatic analysis report
6. Produce professional visualizations

---

# Output

After running the pipeline, the following files will be generated inside:

```
outputs/
```

### Visualizations

```
price_distribution.png
rating_vs_price.png
missing_values.png
price_boxplot.png
top_neighborhoods_price.png
correlation_heatmap.png
```

### AI Generated Report

```
report.txt
```

This report contains **AI-generated insights about the dataset**.

---

# Technologies Used

* Python 3
* Pandas
* Matplotlib
* OpenAI API
* Exploratory Data Analysis (EDA)
* Automated Reporting

---

# Learning Goals of the Project

This project was built to demonstrate:

* Data analysis workflow
* Dataset exploration techniques
* AI-assisted data analysis
* Automated insight generation
* Clean and modular Python project architecture

---

# Author

**Enzo Estévez**

Data Science Student – Universidad Nacional de Luján (UNLU)

Portfolio
https://enzoestevez.com

GitHub
https://github.com/enzoestevez

LinkedIn
https://www.linkedin.com/in/enzoestevez/

---

# Future Improvements

Possible extensions of this project:

* Interactive dashboards using **Plotly or Streamlit**
* Automatic PDF report generation
* Advanced statistical analysis
* AI-driven data storytelling
* Deployment as a web application

---

This project is part of a **Data + AI portfolio series** focused on building real-world analytical tools using Python and modern AI models.
