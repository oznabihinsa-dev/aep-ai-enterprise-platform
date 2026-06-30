from aep.orchestrator.orchestrator import AEPOrchestrator
from aep.orchestrator.task import AEPTask


def test_orchestrator_routes_commercial_offer_with_missing_data():
    orchestrator = AEPOrchestrator()

    task = AEPTask(
        type="commercial_offer",
        payload={
            "company": "ООО ТЕПЛО",
            "customer": "Читинская таможня",
            "product_name": "Уголь 2БПК",
        },
    )

    result = orchestrator.execute(task)

    assert result["service"] == "commercial"
    assert result["status"] == "missing_data"
    assert "volume_tons" in result["missing_fields"]


def test_orchestrator_routes_commercial_offer_ready():
    orchestrator = AEPOrchestrator()

    task = AEPTask(
        type="commercial_offer",
        payload={
            "company": "ООО ТЕПЛО",
            "customer": "Читинская таможня",
            "product_name": "Уголь 2БПК",
            "volume_tons": 100,
            "destination": "Чита",
            "vat_rate": 22,
            "valid_until": "31.12.2026",
        },
    )

    result = orchestrator.execute(task)

    assert result["service"] == "commercial"
    assert result["status"] == "ready_for_generation"
    assert result["missing_fields"] == []


def test_orchestrator_unknown_task():
    orchestrator = AEPOrchestrator()

    task = AEPTask(
        type="unknown",
        payload={},
    )

    result = orchestrator.execute(task)

    assert result["service"] == "unknown"
    assert result["status"] == "unknown_task"