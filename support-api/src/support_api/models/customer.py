from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from datetime import datetime

Plan = Literal["starter", "business", "enterprise"]

class Customer(BaseModel):
    """A customer account - one or many tickets may reference it."""

    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^CUS-\d{5}$")
    name: str = Field(min_length=1, max_length=200)
    tenant: str = Field(min_length=1, max_length=50)
    plan: Plan
    primary_contact_email: str | None = None # name: type = default
    created_at: datetime