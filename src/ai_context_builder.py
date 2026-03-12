# ai_context_builder.py

def build_dataset_context(overview):
    """
    Convert dataset overview into a structured description
    that an AI model can analyze.
    """

    rows = overview["rows"]
    columns = overview["columns"]
    column_names = overview["column_names"]
    missing_values = overview["missing_values"]

    context = f"""
DATASET SUMMARY

Total Rows: {rows}
Total Columns: {columns}

COLUMN NAMES:
"""

    for col in column_names:
        context += f"- {col}\n"

    context += "\nMISSING VALUES:\n"

    missing_found = False

    for col, val in missing_values.items():
        if val > 0:
            context += f"- {col}: {val} missing values\n"
            missing_found = True

    if not missing_found:
        context += "No missing values detected.\n"

    context += """
This dataset appears to contain Airbnb listing information,
including pricing, ratings, and host-related attributes.

Use this context to generate insights.
"""

    return context