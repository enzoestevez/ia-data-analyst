def build_dataset_context(overview):
    """
    Convert dataset overview into a text description
    that an AI model can understand
    """

    rows = overview["rows"]
    columns = overview["columns"]
    column_names = overview["column_names"]
    missing_values = overview["missing_values"]

    context = f"""
Dataset Summary

Rows: {rows}
Columns: {columns}

Column Names:
"""

    for col in column_names:
        context += f"- {col}\n"

    context += "\nColumns with missing values:\n"

    for col, val in missing_values.items():
        if val > 0:
            context += f"- {col}: {val} missing values\n"

    return context