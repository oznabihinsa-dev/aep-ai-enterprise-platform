from aep.services.commercial.models import CommercialOfferRequest
from aep.services.commercial.service import CommercialService


def test_commercial_service_missing_data():
    service = CommercialService()

    request = CommercialOfferRequest(
        company="ООО ТЕПЛО",
        customer="Читинская таможня",
        product_name="Уголь 2БПК",
    )

    result = service.prepare_offer(request)

    assert result.status == "missing_data"
    assert "volume_tons" in result.missing_fields
    assert "destination" in result.missing_fields
    assert "vat_rate" in result.missing_fields
    assert "valid_until" in result.missing_fields


def test_commercial_service_ready_for_generation():
    service = CommercialService()

    request = CommercialOfferRequest(
        company="ООО ТЕПЛО",
        customer="Читинская таможня",
        product_name="Уголь 2БПК",
        volume_tons=100,
        destination="Чита",
        vat_rate=22,
        valid_until="31.12.2026",
    )

    result = service.prepare_offer(request)

    assert result.status == "ready_for_generation"
    assert result.missing_fields == []