from dataclasses import dataclass


@dataclass
class TaskContext:
    company: str
    service: str
    process: str