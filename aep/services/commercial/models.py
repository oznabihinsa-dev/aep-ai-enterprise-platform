from dataclasses import dataclass
from typing import Optional


@dataclass
class CommercialOfferRequest:
    company: str
    customer: str
    product_name: str
    coal_mark: Optional[str] = None
    fraction: Optional[str] = None
    volume_tons: Optional[float] = None
    destination: Optional[str] = None
    delivery_terms: Optional[str] = None
    vat_rate: Optional[float] = None
    valid_until: Optional[str] = None


@dataclass
class CommercialOfferResult:
    status: str
    message: str
    missing_fields: list[str]
    calculated_price_without_vat: Optional[float] = None
    calculated_price_with_vat: Optional[float] = None
    document_path: Optional[str] = None