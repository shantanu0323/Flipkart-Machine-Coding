from enum import Enum
from models.task import Task
from models.task import TaskType
from services.utils import get_date

class FeatureStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    TESTING = 3
    DEPLOYED = 4

class FeatureImpact(Enum):
    LOW = 10
    MODERATE = 11
    HIGH = 12

class FeatureTask(Task):
    def __init__(self, id, title, creator_id, assignee_id, due_date, summary, impact) -> None:
        super().__init__(id, title, creator_id, assignee_id, due_date, FeatureStatus.OPEN, TaskType.FEATURE)
        self.summary = summary
        self.impact = impact

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.creator_id} {self.assignee_id} {self.due_date} {self.summary} {self.impact.name}"

    @classmethod
    def from_string(cls, statement):
        parts = statement.split(" ")
        id = parts[2]
        title = parts[3]
        creator_id = parts[4]
        assignee_id = parts[5]
        due_date = get_date(parts[6])
        summary = parts[7]
        impact = FeatureImpact.LOW
        if parts[8] == "LOW":
            impact = FeatureImpact.LOW
        elif parts[8] == "MODERATE":
            impact = FeatureImpact.MODERATE
        elif parts[8] == "HIGH":
            impact = FeatureImpact.HIGH
        return cls(id, title, creator_id, assignee_id, due_date, summary, impact)

