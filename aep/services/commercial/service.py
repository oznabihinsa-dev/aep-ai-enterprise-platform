from .models import CommercialOfferRequest, CommercialOfferResult
from .validator import CommercialValidator


class CommercialService:
    def __init__(self):
        self.validator = CommercialValidator()

    def prepare_offer(self, request: CommercialOfferRequest) -> CommercialOfferResult:
        missing_fields = self.validator.validate(request)

        if missing_fields:
            return CommercialOfferResult(
                status="missing_data",
                message="Недостаточно данных для подготовки коммерческого предложения.",
                missing_fields=missing_fields,
            )

        return CommercialOfferResult(
            status="ready_for_generation",
            message="Данные проверены. Можно переходить к расчету цены и генерации КП.",
            missing_fields=[],
        )