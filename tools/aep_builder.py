from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRS = [
    "config/employees",
    "config/departments",
    "config/companies",
    "config/processes",
    "config/standards",
    "config/templates",
    "core/entities",
    "core/relations",
    "core/rules",
    "docs/ai-employees",
    "docs/business-processes",
    "docs/architecture",
    "adr",
]

def ensure_dirs():
    for d in DIRS:
        path = ROOT / d
        path.mkdir(parents=True, exist_ok=True)
        readme = path / "README.md"
        if not readme.exists():
            readme.write_text(f"# {d}\n", encoding="utf-8")

def main():
    ensure_dirs()
    print("AEP Builder: structure checked successfully.")

if __name__ == "__main__":
    main()