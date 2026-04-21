import re
import pandas as pd

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase snake_case"""
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", "_", regex=True)
    )
    return df

def clean_text_columns(df: pd.DataFrame, text_columns: list[str]) -> pd.DataFrame:
    """Strip whitespace from selected text columns and restore missing values"""
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace("nan", pd.NA)
    return df

def standardize_text_format(df: pd.DataFrame) -> pd.DataFrame:
    """Apply title casing to selected text fields"""
    for col in ["first_name", "last_name", "city", "country"]:
        if col in df.columns:
            df[col] = df[col].str.title()
    return df

def validate_emails(df: pd.DataFrame) -> pd.DataFrame:
    """Keep only rows with valid-looking email addresses"""
    if "email" in df.columns:
        df["email"] = df["email"].astype(str).str.strip().str.lower()
        df = df[df["email"].str.contains("@", na=False)]
        df.loc[df["email"] == "nan", "email"] = pd.NA
    return df

def clean_phone(phone):
    """Remove non-digit characters from phone numbers"""
    if pd.isna(phone):
        return phone
    return re.sub(r"\D", "", str(phone))

def normalize_phone_numbers(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize phone columns by keeping only digits"""
    for col in ["phone_1", "phone_2"]:
        if col in df.columns:
            df[col] = df[col].apply(clean_phone)
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows missing essential values and fill missing company values"""
    essential_columns = [
        col for col in ["first_name", "last_name", "email"] if col in df.columns
    ]

    if essential_columns:
        df = df.dropna(subset=essential_columns)

    if "company" in df.columns:
        df["company"] = df["company"].fillna("Unknown")

    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove dupicate customer records based on email"""
    if "email" in df.columns:
        df = df.drop_duplicates(subset=["email"])
    return df

def convert_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Convert subscription_date to datetime format"""
    if "subscription_date" in df.columns:
        df["subscription_date"] = df.to_datetime(
            df["subscription_date"],
            errors="coerce"
        )
    return df
