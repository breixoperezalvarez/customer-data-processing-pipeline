import pandas as pd

def add_full_name(df: pd.DataFrame) -> pd.DataFrame:
    """Create a full_name column"""
    if "first_name" in df.columns and "last_name" in df.columns:
        df["full_name"] = df["first_name"] + " " + df["last_name"]
    return df

def add_name_length(df: pd.DataFrame) -> pd.DataFrame:
    """Create a name_length column"""
    if "full_name" in df.columns:
        df["name_length"] = df["full_name"].apply(len)
    return df

def add_email_domain(df: pd.DataFrame) -> pd.DataFrame:
    """Extract the domain from the email address"""
    if "email" in df.columns:
        df["email_domain"] = df["email"].apply(
            lambda x: x.split("@")[-1] if pd.notna(x) else pd.NA
        )
    return df

def add_has_company(df: pd.DataFrame) -> pd.DataFrame:
    """Create a boolean column showing if company information exists"""
    if "company" in df.columns:
        df["has_company"] = df["company"].apply(lambda x: x != "Unknown")
    return df

def add_subscription_year(df: pd.DataFrame) -> pd.DataFrame:
    """Extract subscription year from subscription_date"""
    if "subscription_date" in df.columns:
        df["subscription_year"] = df["subscription_date"].dt.year
    return df