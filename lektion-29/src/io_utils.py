import pandas as pd

REQUIRED = [
    "loan_id","checkout_date","branch","genre","item_type",
    "patron_age_group","loan_days","returned_date","overdue_days","fine_amount"
]

def load_data(path: str) -> pd.DataFrame:
    """
    Läser CSV och gör datumkolumner till datetime.
    """
    df = pd.read_csv(path, parse_dates=["checkout_date", "returned_date"])
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Saknade kolumner: {missing}")
    return df

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Säkerställer att numeriska kolumner faktiskt är numeriska.
    """
    out = df.copy()
    for c in ["loan_days", "overdue_days", "fine_amount"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    return out    
