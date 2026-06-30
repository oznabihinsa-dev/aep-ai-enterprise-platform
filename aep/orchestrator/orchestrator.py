from .router import ServiceRouter
from aep.services.commercial.models import CommercialOfferRequest
from aep.services.commercial.service import CommercialService


class AEPOrchestrator:
    """
    Центральный координатор платформы AEP.
    """

    def __init__(self):
        self.router = ServiceRouter()
        self.commercial_service = CommercialService()

    def execute(self, task):
        service_name = self.router.resolve(task)

        if service_name == "commercial":
            request = CommercialOfferRequest(**task.payload)
            result = self.commercial_service.prepare_offer(request)

            return {
                "service": service_name,
                "status": result.status,
                "message": result.message,
                "missing_fields": result.missing_fields,
            }

        return {
            "service": "unknown",
            "status": "unknown_task",
        }