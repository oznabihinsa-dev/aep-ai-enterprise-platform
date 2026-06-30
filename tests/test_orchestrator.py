from aep.orchestrator.orchestrator import AEPOrchestrator
from aep.orchestrator.task import AEPTask


def test_orchestrator_routes_commercial_offer():
    orchestrator = AEPOrchestrator()

    task = AEPTask(
        type="commercial_offer",
        payload={
            "company": "ООО ТЕПЛО",
            "customer": "Читинская таможня",
        },
    )

    result = orchestrator.execute(task)

    assert result["service"] == "commercial"
    assert result["status"] == "routed"


def test_orchestrator_unknown_task():
    orchestrator = AEPOrchestrator()

    task = AEPTask(
        type="unknown",
        payload={},
    )

    result = orchestrator.execute(task)

    assert result["service"] == "unknown"
    assert result["status"] == "unknown_task"