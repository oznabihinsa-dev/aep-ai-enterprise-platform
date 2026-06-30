from .models import CommercialOfferRequest


class CommercialValidator:
    required_fields = [
        "company",
        "customer",
        "product_name",
        "volume_tons",
        "destination",
        "vat_rate",
        "valid_until",
    ]

    def validate(self, request: CommercialOfferRequest) -> list[str]:
        missing = []

        for field in self.required_fields:
            value = getattr(request, field, None)
            if value is None or value == "":
                missing.append(field)

        return missing