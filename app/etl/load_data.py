import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Credentials
USERNAME = "postgres"
PASSWORD = "5432"
HOST = "localhost"
PORT = "5432"
DATABASE = "supplymind_ai"

DATABASE_URL = (
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

engine = create_engine(DATABASE_URL)

# Dictionary of tables and CSV files
files = {
    "customers": "data/processed/customers.csv",
    "products": "data/processed/products.csv",
    "orders": "data/processed/orders.csv",
    "order_items": "data/processed/order_items.csv",
    "shipments": "data/processed/shipments.csv",
    "financials": "data/processed/financials.csv",
    "locations": "data/processed/locations.csv"
}

for table_name, file_path in files.items():
    print(f"Loading {table_name}...")

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✅ {table_name} loaded successfully!")

print("\n🎉 All tables loaded into PostgreSQL!")