# Data cleaning
import pandas as pd

# ============================================================
# Practical 5 - Data cleaning (Medical Federal Government Salaries)
# ============================================================
import os
import pandas as pd

INPUT_PATH = r"C:\Users\admin\Downloads\salaries.csv\salaries.csv"
OUTPUT_DIR = r"C:\Users\admin\Downloads"

FILTERED_OUTPUT = os.path.join(OUTPUT_DIR, "Mex Federal Government Salaries CDMX.csv")
CLEANED_OUTPUT = os.path.join(OUTPUT_DIR, "Mex Federal Government Salaries CDMX cleaned.csv")

if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"Could not find file at: {INPUT_PATH}")

df = pd.read_csv(
    INPUT_PATH,
    na_values="n/a",
    parse_dates=["periodoreportainicio", "periodoreportafin"]
)

print("Raw data loaded:")
df.info()

df = df[df["entidadfederativa"] == "Ciudad de México"].copy()

for col in ["level_0", "index"]:
    if col in df.columns:
        df.drop(columns=col, inplace=True)

print(f"\nFiltered to Ciudad de México: {len(df)} rows")
print(df.head(5))

df.to_csv(FILTERED_OUTPUT, index=False)
print(f"\nSaved filtered file to: {FILTERED_OUTPUT}")

text_cols = [
    "entidadfederativa", "sujetoobligado", "nombre", "denominacion",
    "cargo", "area", "periodoreportainicio", "periodoreportafin"
]
text_cols = [c for c in text_cols if c in df.columns]  # only clean cols that exist

df[text_cols] = df[text_cols].apply(lambda x: x.astype(str).str.strip().str.title())
df[text_cols] = df[text_cols].apply(lambda x: x.str.replace("De", "de", regex=False))

rename_map = {
    "entidadfederativa": "Entidad_Federativa",
    "sujetoobligado": "Sujeto_Obligado",
    "nombre": "Nombre",
    "denominacion": "Denominacion",
    "montoneto": "Monto_Neto",
    "cargo": "Cargo",
    "area": "Area",
    "montobruto": "Monto_Bruto",
    "idInformacion": "ID",
    "periodoreportainicio": "Periodo_Reporta_Inicio",
    "periodoreportafin": "Periodo_Reporta_Fin",
}
df.rename(columns=rename_map, inplace=True)

print("\nAfter renaming:")
print(df.head(5))

desired_order = [
    "ID", "Nombre", "Cargo", "Area", "Denominacion", "Sujeto_Obligado",
    "Entidad_Federativa", "Monto_Bruto", "Monto_Neto",
    "Periodo_Reporta_Inicio", "Periodo_Reporta_Fin"
]
desired_order = [c for c in desired_order if c in df.columns]
df = df.reindex(columns=desired_order)

print("\nFinal column order:")
print(df.head(3))

def get_row_by_id(df, id_value):
    """Return the row matching a given ID."""
    return df.loc[df["ID"] == id_value]


def employee_info(df, id_value):
    """Return a readable summary sentence for a given employee ID."""
    row = df.loc[df["ID"] == id_value]
    if row.empty:
        return f"No employee found with ID {id_value}."

    tax = row["Monto_Bruto"].values[0] - row["Monto_Neto"].values[0]
    return (
        f"{row['Nombre'].values[0]} was a {row['Cargo'].values[0]} that worked in "
        f"{row['Entidad_Federativa'].values[0]} between {row['Periodo_Reporta_Inicio'].values[0]} "
        f"and {row['Periodo_Reporta_Fin'].values[0]}. This employee paid ${tax:,.2f} MX "
        f"in tax every month."
    )


# Example usage:
print("\n--- Example lookups ---")
print(get_row_by_id(df, 18698843))
print(get_row_by_id(df, 19091192))
print(employee_info(df, 19091192))
print(employee_info(df, 19918891))

df.to_csv(CLEANED_OUTPUT, index=False)
print(f"\nSaved cleaned file to: {CLEANED_OUTPUT}")


# ============================================================
# Practical 6 (Q3) - Missing values & duplicates
# ============================================================
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Amit"],
    "Age": [25, None, 30, 28, 25],
    "City": ["Pune", "Mumbai", None, "Pune", "Pune"],
    "Salary": [45000, 55000, None, 60000, 45000]
}

df = pd.DataFrame(data)

print("Missing values:")
print(df.isnull())

print("\nMissing values in each column:")
print(df.isnull().sum())

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].median())
print(df)

df["City"] = df["City"].fillna("Unknown")
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df)

print("\nDataFrame after cleaning:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDoes the DataFrame contain missing values?")
print(df.isnull().values.any())
