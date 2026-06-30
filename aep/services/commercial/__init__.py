class CommercialService:
    def __init__(self):
        self.validator = CommercialValidator()
        self.document_generator = DocumentGenerator()

        self.context_builder = CommercialContextBuilder(
            price_repo=PriceRepository(
                Settings.paths.PRICE / "Расчет цены на 2026 год.xlsx"
            ),
            template_repo=TemplateRepository(
                Settings.paths.TEMPLATES
            ),
            certificate_repo=CertificateRepository(
                Settings.paths.CERTIFICATES
            ),
        )