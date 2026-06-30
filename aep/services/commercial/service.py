from .models import CommercialOfferRequest, CommercialOfferResult
from .validator import CommercialValidator
from .context_builder import CommercialContextBuilder
from .price_repository import PriceRepository
from .template_repository import TemplateRepository
from .certificate_repository import CertificateRepository


class CommercialService:
    def __init__(self):
        self.validator = CommercialValidator()
        self.context_builder = CommercialContextBuilder(
            price_repo=PriceRepository("sample_data/price/Расчет цены на 2026 год.xlsx"),
            template_repo=TemplateRepository("sample_data/templates"),
            certificate_repo=CertificateRepository("sample_data/certificates"),
        )

    def prepare_offer(self, request: CommercialOfferRequest) -> CommercialOfferResult:
        missing_fields = self.validator.validate(request)

        if missing_fields:
            return CommercialOfferResult(
                status="missing_data",
                message="Недостаточно данных для подготовки коммерческого предложения.",
                missing_fields=missing_fields,
            )

        context = self.context_builder.build(request)

        return CommercialOfferResult(
            status="context_built",
            message="Контекст КП собран. Готов к генерации документа.",
            missing_fields=[],
            calculated_price_without_vat=context.calculated_price_without_vat,
            calculated_price_with_vat=context.calculated_price_with_vat,
            document_path=str(context.template_path),
            calculation={
                "base_price": context.base_price,
                "template_path": str(context.template_path),
                "certificate_path": str(context.certificate_path),
            },
        )