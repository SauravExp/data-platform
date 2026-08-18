import pandas as pd
from pathlib import Path
# Resolves the path relative to the root folder
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

customers = pd.read_csv(DATA_DIR / "olist_customers_dataset.csv")
geolocation = pd.read_csv(DATA_DIR / "olist_geolocation_dataset.csv")
order_items = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")
order_payments = pd.read_csv(DATA_DIR / "olist_order_payments_dataset.csv")
order_reviews = pd.read_csv(DATA_DIR / "olist_order_reviews_dataset.csv")
orders = pd.read_csv(DATA_DIR / "olist_orders_dataset.csv")
products = pd.read_csv(DATA_DIR / "olist_products_dataset.csv")
sellers = pd.read_csv(DATA_DIR / "olist_sellers_dataset.csv")
category_translation = pd.read_csv(
    DATA_DIR / "product_category_name_translation.csv"
)

## CHECK FOR RECORDS
tables = {
    "customers": customers,
    "geolacation" : geolocation,
    "order_items" : order_items,
    "order_payments" : order_payments,
    "order_reviews" : order_reviews,
    "orders" : orders,
    "products" : products,
    "sellers" : sellers,
    "category_translation" : category_translation
}

for name, df in tables.items():
    print(f"{name}: {len(df):,} rows ")

##CHECK FOR COLUMNS 
for name, df in tables.items():
    print("\n"+ "="*60)
    print(name)
    print("="*60)
    print(df.columns.tolist())

## TO CHECK DATA TYPES
for name, df in tables.items():
    print("\n" + "="*60)
    print(name)
    print("="*60)
    print(df.dtypes)
    orders.info()

## TO CHECK THE MISSING VALUES
for name, df in tables.items():
    print("\n" + "="*60)
    print(name+ " \t\t- Missing Values")
    print("="*60)
    print(df.isnull().sum())
###This will tell you which columns contain NULL/missing values

## TO CHECK THE DUPLICATE RECORDS
for name, df in tables.items():
    print("\n" + "="*60)
    print(name + " \t\t- Duplicate Records")
    print("="*60)
    print(df.duplicated().sum())

orders.head()
customers.head()
order_items.head()
