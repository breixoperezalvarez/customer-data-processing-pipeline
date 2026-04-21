import pandas as pd

def generate_report(df_before: pd.DataFrame, df_after: pd.DataFrame, output_path: str) -> None:
    """Generate a summary report for the customer data pipeline"""
    lines = []

    # Header
    lines.append("CUSTOMER DATA PROCESSING REPORT")
    lines.append("=" * 40)
    lines.append("")

    # Basic info
    lines.append(f"Rows before cleaning: {len(df_before)}")
    lines.append(f"Rows after cleaning: {len(df_after)}")
    lines.append(f"Rows removed: {len(df_before) - len(df_after)}")
    lines.append("")

    # Columns
    lines.append("Columns after processing:")
    for column in df_after.columns:
        lines.append(f"- {column}")

    lines.append("")

    # Missing values
    lines.append("Missing values after cleaning:")
    missing_values = df_after.isna().sum()
    for column, count in missing_values.items():
        lines.append(f"- {column}: {count}")

    # Top countries
    if "country" in df_after.columns:
        lines.append("")
        lines.append("Top 5 countries:")
        for country, count in df_after["country"].value_counts().head(5).items():
            lines.append(f"- {country}: {count}")

    # Email domains
    if "email_domain" in df_after.columns:
        lines.append("")
        lines.append("Top 5 email domains:")
        for domain, count in df_after["email_domain"].value_counts().head(5).items():
            lines.append(f"- {domain}: {count}")

    # Subscription trends
    if "subscription_year" in df_after.columns:
        lines.append("")
        lines.append("Subscriptions by year:")
        year_counts = df_after["subscription_year"].value_counts().sort_index()
        for year, count in year_counts.items():
            lines.append(f"- {year}: {count}")

    # Write file
    with open(output_path, "w", encoding="uft-8") as file:
        file.write("\n".join(lines))
