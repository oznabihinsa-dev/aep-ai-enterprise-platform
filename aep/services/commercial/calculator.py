class PriceCalculator:

    def calculate(self, base_price, transfer, delivery, vat_rate):
        total_without_vat = base_price + transfer + delivery
        vat_amount = total_without_vat * (vat_rate / 100)
        total_with_vat = total_without_vat + vat_amount

        return {
            "total_without_vat": round(total_without_vat, 2),
            "vat_amount": round(vat_amount, 2),
            "total_with_vat": round(total_with_vat, 2),
        }