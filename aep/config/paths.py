from pathlib import Path


class Paths:
    ROOT = Path(__file__).resolve().parents[2]

    SAMPLE_DATA = ROOT / "sample_data"

    PRICE = SAMPLE_DATA / "price"

    TEMPLATES = SAMPLE_DATA / "templates"

    CERTIFICATES = SAMPLE_DATA / "certificates"

    OUTPUT = ROOT / "output"