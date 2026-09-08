from sqlalchemy import create_engine

# PostgreSQL Credentials
USERNAME = "postgres"
PASSWORD = "5432"
HOST = "localhost"
PORT = "5432"
DATABASE = "supplymind_ai"

# Connection String
DATABASE_URL = (
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

# Create Engine
engine = create_engine(DATABASE_URL)

# Test Connection
try:
    with engine.connect() as conn:
        print("✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Connection failed!")
    print(e)