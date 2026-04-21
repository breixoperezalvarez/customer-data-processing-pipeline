# Customer Data Processing Pipeline

This project implements a Python-based data processing pipeline for cleaning, validating, and analyzing large-scale customer data. It processes a dataset containing 100,000+ customer records and produces a cleaned dataset along with a summary report of key insights.

---

## Features

- Load raw CSV customer data
- Standardize column names (snake_case)
- Clean and normalize text fields
- Validate email addresses
- Normalize phone numbers
- Remove duplicate records
- Handle missing values
- Convert date columns to datetime format
- Perform feature engineering
- Generate cleaned dataset
- Produce automated summary report

---

## Dataset

In this case I chose a sample csv data generator from https://github.com/datablist/sample-csv-files, since it is more convenient for this kind of project.

The dataset includes the following fields:

- Index  
- Customer Id  
- First Name  
- Last Name  
- Company  
- City  
- Country  
- Phone 1  
- Phone 2  
- Email  
- Subscription Date  
- Website  

After processing, column names are standardized to:
index, customer_id, first_name, last_name, company, city,
country, phone_1, phone_2, email, subscription_date, website

---

## Pipeline Steps

1. Load raw CSV data  
2. Standardize column names  
3. Clean text fields (names, city, country, etc.)  
4. Validate email addresses  
5. Normalize phone numbers  
6. Remove duplicate records  
7. Handle missing values  
8. Convert dates to datetime format  
9. Create new features:
   - full_name  
   - name_length  
   - email_domain  
   - has_company  
   - subscription_year  
10. Export cleaned dataset  
11. Generate summary report  

---

## Example Results

- Rows before cleaning: 100000  
- Rows after cleaning: (replace with your result)  
- Rows removed: (replace with your result)  

### Sample Insights

- Top countries by customer count  
- Most common email domains  
- Subscription trends over time  

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the pipeline

python src/main.py
