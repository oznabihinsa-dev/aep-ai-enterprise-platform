from .router import ServiceRouter


class AEPOrchestrator:
    """
    Центральный координатор платформы AEP.
    """

    def __init__(self):
        self.router = ServiceRouter()

    def execute(self, task):
        service_name = self.router.resolve(task)

        return {
            "service": service_name,
            "status": "routed" if service_name != "unknown" else "unknown_task",
        }