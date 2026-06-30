class ServiceRouter:
    """
    Определяет, какой сервис должен обработать задачу.
    """

    def resolve(self, task):
        task_type = getattr(task, "type", None)

        if task_type == "commercial_offer":
            return "commercial"

        return "unknown"