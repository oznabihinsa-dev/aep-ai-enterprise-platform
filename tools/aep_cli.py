from aep.orchestrator.orchestrator import AEPOrchestrator
from aep.orchestrator.task import AEPTask


def main():
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

    print(result)


if __name__ == "__main__":
    main()