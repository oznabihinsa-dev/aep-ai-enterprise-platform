from pathlib import Path


class CertificateRepository:
    def __init__(self, certificates_dir: str | Path):
        self.certificates_dir = Path(certificates_dir)

    def find_certificate(self, coal_mark: str) -> Path:
        if not self.certificates_dir.exists():
            raise FileNotFoundError(f"Папка сертификатов не найдена: {self.certificates_dir}")

        normalized_mark = coal_mark.lower().replace(" ", "")
        candidates = list(self.certificates_dir.glob("*.pdf"))

        for candidate in candidates:
            name = candidate.name.lower().replace(" ", "")
            if normalized_mark in name:
                return candidate

        raise FileNotFoundError(f"Сертификат для марки {coal_mark} не найден")