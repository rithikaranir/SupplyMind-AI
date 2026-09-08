from app.database import SessionLocal
from fastapi import HTTPException
from app.models import PredictionLog
from fastapi import FastAPI
from sqlalchemy import func
from app.models import PredictionLog
import pandas as pd

from app.schemas import DeliveryInput
from app.model_loader import (
    model,
    preprocessor,
    threshold
)


app = FastAPI(
    title="SupplyMind AI",
    description="Late Delivery Prediction API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "SupplyMind AI API Running"
    }


@app.post("/predict")
def predict(data: DeliveryInput):

    try:

        input_data = pd.DataFrame(
            [data.dict()]
        )

        transformed_data = preprocessor.transform(
            input_data
        )

        probability = model.predict_proba(
            transformed_data
        )[0][1]

        prediction = int(
            probability >= threshold
        )


        db = SessionLocal()

        log = PredictionLog(
            shipping_mode=data.shipping_mode,
            market=data.market,
            order_region=data.order_region,
            customer_segment=data.customer_segment,
            category_name=data.category_name,
            quantity=data.quantity,
            order_total=data.order_total,
            prediction=prediction,
            risk_probability=float(probability)
        )

        db.add(log)
        db.commit()
        db.close()


        return {
            "late_delivery_prediction": prediction,
            "risk_probability": round(float(probability), 3),
            "risk_level": "High" if prediction == 1 else "Low"
        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@app.get("/dashboard/summary")
def dashboard_summary():

    db = SessionLocal()

    total = db.query(
        PredictionLog
    ).count()


    high_risk = db.query(
        PredictionLog
    ).filter(
        PredictionLog.prediction == 1
    ).count()


    low_risk = db.query(
        PredictionLog
    ).filter(
        PredictionLog.prediction == 0
    ).count()


    db.close()


    return {
        "total_predictions": total,
        "high_risk": high_risk,
        "low_risk": low_risk
    }

@app.get("/dashboard/shipping-risk")
def shipping_risk():

    db = SessionLocal()

    result = (
        db.query(
            PredictionLog.shipping_mode,
            func.count(PredictionLog.id).label("total"),
            func.sum(PredictionLog.prediction).label("late")
        )
        .group_by(
            PredictionLog.shipping_mode
        )
        .all()
    )

    db.close()


    data = []

    for row in result:

        late_percentage = (
            (row.late / row.total) * 100
            if row.total > 0
            else 0
        )

        data.append({
            "shipping_mode": row.shipping_mode,
            "total_orders": row.total,
            "late_orders": row.late,
            "late_percentage": round(
                late_percentage,
                2
            )
        })


    return data

@app.get("/dashboard/region-risk")
def region_risk():

    db = SessionLocal()

    result = (
        db.query(
            PredictionLog.order_region,
            func.count(PredictionLog.id).label("total"),
            func.sum(PredictionLog.prediction).label("late")
        )
        .group_by(
            PredictionLog.order_region
        )
        .all()
    )

    db.close()


    data = []

    for row in result:

        late_percentage = (
            (row.late / row.total) * 100
            if row.total > 0
            else 0
        )

        data.append({
            "region": row.order_region,
            "total_orders": row.total,
            "late_orders": row.late,
            "late_percentage": round(
                late_percentage,
                2
            )
        })


    return data