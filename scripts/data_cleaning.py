import pandas as pd

def rename_columns(data):
    """Rename columns to lowercase, remove spaces and normalize."""
    data.columns = [col.strip().lower().replace(" ", "_") for col in data.columns]
    return data

def convert_dates(data):
    """Convert 'fecha_nacimiento' to datetime format."""
    data['fecha_nacimiento'] = pd.to_datetime(data['fecha_nacimiento'], format='%m%Y', errors='coerce')
    return data

def handle_missing_values(data):
    """Handle missing values by filling with defaults."""
    data.fillna({
        'bea': 'No',  # Fill 'bea' with 'No' if missing
        'pace': 'No',  # Fill 'pace' with 'No' if missing
        'ingreso_percapita_grupo_fa': 0  # Fill 'ingreso_percapita_grupo_fa' with 0 if missing
    }, inplace=True)
    return data

def convert_data_types(data):
    """Convert appropriate columns to integer or other specific types."""
    data['rbd'] = data['rbd'].astype(int, errors='ignore')
    data['codigo_region'] = data['codigo_region'].astype(int, errors='ignore')
    return data

def clean_data(input_path, output_path):
    """Main function to clean the dataset."""
    # Load the dataset
    data = pd.read_csv(input_path, sep=';')

    # Apply cleaning functions
    data = rename_columns(data)
    data = convert_dates(data)
    data = handle_missing_values(data)
    data = convert_data_types(data)

    # Remove duplicates if they exist
    data.drop_duplicates(inplace=True)

    # Save cleaned data to output path
    data.to_csv(output_path, index=False)
    print(f"Data cleaning complete. Cleaned data saved to {output_path}")

# If running as a script
if __name__ == "__main__":
    input_file = 'C:/Users/BS/Documents/PAES2025_Admissions_Analysis/data/raw/admissions_data_2025.csv'
    output_file = 'C:/Users/BS/Documents/PAES2025_Admissions_Analysis/data/processed/clean_admissions_data_2025.csv'
    clean_data(input_file, output_file)
