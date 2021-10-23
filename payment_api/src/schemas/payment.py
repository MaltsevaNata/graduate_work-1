from src.models import PaymentState
from src.schemas import AbstractSchema


class PaymentSchema(AbstractSchema):
    id: int
    invoice_id: str
    product_id: str
    user_id: str
    status: PaymentState

    class Config:
        orm_mode = True
        use_enum_values = True


class AddPaymentSchema(AbstractSchema):
    user_id: str
    product_id: str
    amount: str
    currency: str = "RUB"


class NewPaymentSchema(AbstractSchema):
    product: str
    currency: str = "RUB"


class UpdatePaymentSchema(AbstractSchema):
    invoice_id: str
    status: PaymentState

    class Config:
        use_enum_values = True


class NewPaymentResult(AbstractSchema):
    id: str
    client_secret: str


class PaymentCancel(AbstractSchema):
    user_id: str
    amount: int
    currency: str = "RUB"
