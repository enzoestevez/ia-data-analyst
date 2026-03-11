from src.data_loader import load_dataset, get_dataset_overview
from src.ai_context_builder import build_dataset_context
from src.ai_agent import ask_ai_about_dataset
from src.report_generator import generate_report

df = load_dataset("data/airbnb.csv")

overview = get_dataset_overview(df)

print("\nDATASET OVERVIEW")
print("-------------------")

print(f"Rows: {overview['rows']}")
print(f"Columns: {overview['columns']}")

print("\nColumn Names:")
for col in overview["column_names"]:
    print(f"- {col}")

print("\nMissing Values:")
for col, val in overview["missing_values"].items():
    print(f"{col}: {val}")

context = build_dataset_context(overview)

print("\nAI DATASET CONTEXT")
print("-------------------")
print(context)


question = "What interesting insights could we explore from this Airbnb dataset?"
ai_response = ask_ai_about_dataset(context, question)

print("\nAI ANALYSIS")
print("-------------------")
print(ai_response)

questions = [
    "What interesting insights could we explore from this Airbnb dataset?",
    "Which columns have the most missing values and how could we handle them?",
    "Suggest visualizations that could be useful for this dataset"
]

report = generate_report(context, questions)

print("\nAUTOMATIC REPORT")
print("-------------------")
print(report)