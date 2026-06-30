from dataclasses import dataclass


@dataclass
class AEPTask:
    type: str
    payload: dict