from docx import Document
from pathlib import Path
from .context import CommercialOfferContext


class DocumentGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate(self, context: CommercialOfferContext) -> Path:
        doc = Document()

        doc.add_heading("Коммерческое предложение", level=1)

        doc.add_paragraph(f"Компания: {context.request.company}")
        doc.add_paragraph(f"Заказчик: {context.request.customer}")
        doc.add_paragraph(f"Продукт: {context.request.product_name}")
        doc.add_paragraph(f"Марка угля: {context.request.coal_mark}")
        doc.add_paragraph(f"Объем: {context.request.volume_tons} тонн")
        doc.add_paragraph(f"Пункт поставки: {context.request.destination}")

        doc.add_paragraph("")
        doc.add_paragraph("=== РАСЧЕТ ===")

        doc.add_paragraph(f"Базовая цена: {context.base_price}")
        doc.add_paragraph(f"Без НДС: {context.calculated_price_without_vat}")
        doc.add_paragraph(f"С НДС: {context.calculated_price_with_vat}")

        doc.add_paragraph("")
        doc.add_paragraph(f"Шаблон: {context.template_path}")
        doc.add_paragraph(f"Сертификат: {context.certificate_path}")

        file_path = self.output_dir / "commercial_offer.docx"
        doc.save(file_path)

        return file_path