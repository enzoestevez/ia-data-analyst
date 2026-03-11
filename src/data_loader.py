import pandas as pd

def load_dataset(file_path):
    """
    Load a dataset from a CSV file
    """
    df = pd.read_csv(file_path, sep=";", on_bad_lines="skip")
    return df


def get_dataset_overview(df):
    """
    Generate a basic overview of the dataset
    """
    overview = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }

    return overview


def summarize_dataset(df):
    """
    Generate descriptive statistics
    """
    summary = df.describe(include="all").to_dict()
    return summary