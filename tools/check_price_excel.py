from aep.services.commercial.price_repository import PriceRepository


repo = PriceRepository("sample_data/price/Расчет цены на 2026 год.xlsx", year="2026")

row = repo.find_price(
    destination="Кадала",
    coal_mark="2БПК",
    vat="без НДС",
)

print(row)