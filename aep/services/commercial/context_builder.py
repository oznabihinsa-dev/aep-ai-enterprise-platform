from .context import CommercialOfferContext
from .price_repository import PriceRepository
from .template_repository import TemplateRepository
from .certificate_repository import CertificateRepository


class CommercialContextBuilder:
    def __init__(
        self,
        price_repo: PriceRepository,
        template_repo: TemplateRepository,
        certificate_repo: CertificateRepository,
    ):
        self.price_repo = price_repo
        self.template_repo = template_repo
        self.certificate_repo = certificate_repo

    def build(self, request):
        price_row = self.price_repo.find_price(
            destination=request.destination,
            coal_mark=request.coal_mark,
        )

        certificate_path = self.certificate_repo.find_certificate(
            request.coal_mark
        )

        template_path = self.template_repo.find_commercial_offer_template()

        base_price = price_row["price"]

        vat_rate = request.vat_rate or 20

        total_without_vat = base_price * request.volume_tons
        total_with_vat = total_without_vat * (1 + vat_rate / 100)

        return CommercialOfferContext(
            request=request,
            base_price=base_price,
            calculated_price_without_vat=round(total_without_vat, 2),
            calculated_price_with_vat=round(total_with_vat, 2),
            template_path=template_path,
            certificate_path=certificate_path,
        )