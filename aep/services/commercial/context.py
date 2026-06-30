from dataclasses import dataclass
from pathlib import Path

from .models import CommercialOfferRequest


@dataclass
class CommercialOfferContext:
    request: CommercialOfferRequest

    base_price: float

    calculated_price_without_vat: float
    calculated_price_with_vat: float

    template_path: Path
    certificate_path: Path