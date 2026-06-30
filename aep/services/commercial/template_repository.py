from pathlib import Path


class TemplateRepository:
    def __init__(self, templates_dir: str | Path):
        self.templates_dir = Path(templates_dir)

    def find_commercial_offer_template(self) -> Path:
        if not self.templates_dir.exists():
            raise FileNotFoundError(f"Папка шаблонов не найдена: {self.templates_dir}")

        candidates = list(self.templates_dir.glob("*.docx"))

        if not candidates:
            raise FileNotFoundError(
                f"В папке {self.templates_dir} не найден ни один DOCX-шаблон"
            )

        for candidate in candidates:
            name = candidate.name.lower()
            if "commercial" in name or "кп" in name or "offer" in name:
                return candidate

        return candidates[0]