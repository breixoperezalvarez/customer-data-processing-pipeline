import os

from load_data import load_csv
from clean_data import (
    standardize_column_names,
    clean_text_columns,
    standardize_text_format,
    validate_emails,
    normalize_phone_numbers,
    handle_missing_values,
    remove_duplicates,
    convert_dates
)
from feature_engineering import (
    add_full_name,
    add_name_length,
    add_email_domain,
    add_has_company,
    add_subscription_year
)
from report import generate_report

def main() -> None:
    raw_file_path = "data/raw/customers-100000.csv"
    cleaned_file_path = "data/processed/cleaned_customers.csv"
    report_file_path = "output/summary_report.txt"

    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("output", exists_ok=True)

    df = load_csv(raw_file_path)

    print("Original columns:")
    print(df.columns)

    df = standardize_column_names(df)

    print("\nStandardized columns:")
    print(df.columns)

    df_before = df.copy()

    df = clean_text_columns(
        df,
        ["first_name", "last_name", "company", "city", "country", "website"]
    )
    df = standardize_text_format(df)
    df = validate_emails(df)
    df = normalize_phone_numbers(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = convert_dates(df)

    df = add_full_name(df)
    df = add_name_length(df)
    df = add_email_domain(df)
    df = add_has_company(df)
    df = add_subscription_year(df)

    df.to_csv(cleaned_file_path, index=False)
    generate_report(df_before, df, report_file_path)

    print("\nPipeline completed successfully.")
    print(f"Cleaned data saved to. {cleaned_file_path}")
    print(f"Summary report saved to: {report_file_path}")

if __name__== "__main__":
    main()