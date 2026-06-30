from .models import CommercialOfferRequest, CommercialOfferResult
from .validator import CommercialValidator
from .calculator import PriceCalculator


class CommercialService:
    def __init__(self):
        self.validator = CommercialValidator()
        self.calculator = PriceCalculator()

    def prepare_offer(self, request: CommercialOfferRequest) -> CommercialOfferResult:
        missing_fields = self.validator.validate(request)

        if missing_fields:
            return CommercialOfferResult(
                status="missing_data",
                message="Недостаточно данных для подготовки коммерческого предложения.",
                missing_fields=missing_fields,
            )

        calc = self.calculator.calculate(
            base_price=2844.58,
            transfer=350,
            delivery=600,
            vat_rate=request.vat_rate,
        )

        return CommercialOfferResult(
            status="calculated",
            message="Цена рассчитана. Можно переходить к генерации КП.",
            missing_fields=[],
            calculated_price_without_vat=calc["total_without_vat"],
            calculated_price_with_vat=calc["total_with_vat"],
            calculation=calc,
        )