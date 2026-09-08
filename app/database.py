from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://postgres:5432@localhost:5432/supplymind_ai"
)


engine = create_engine(
    DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)