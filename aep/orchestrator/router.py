class ServiceRouter:
    """
    Определяет, какой сервис должен обработать задачу.
    """

    def resolve(self, task):
        raise NotImplementedError