from pydantic import BaseModel


class DeliveryInput(BaseModel):

    shipping_mode: str
    scheduled_shipping_days: int
    market: str
    order_region: str
    customer_segment: str
    category_name: str
    quantity: int
    order_total: float