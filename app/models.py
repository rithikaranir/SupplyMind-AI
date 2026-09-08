from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from app.database import engine
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class PredictionLog(Base):

    __tablename__ = "prediction_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    shipping_mode = Column(String)
    market = Column(String)
    order_region = Column(String)
    customer_segment = Column(String)
    category_name = Column(String)

    quantity = Column(Integer)

    order_total = Column(Float)

    prediction = Column(Integer)

    risk_probability = Column(Float)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )


Base.metadata.create_all(
    bind=engine
)