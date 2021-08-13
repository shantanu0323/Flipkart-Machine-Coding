from enum import Enum
from models.task import Task
from models.task import TaskType
from services.utils import get_date

class BugStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    FIXED = 3

class BugSeverity(Enum):
    P0 = 10
    P1 = 11
    P2 = 12

class BugTask(Task):
    def __init__(self, id, title, creator_id, assignee_id, due_date, severity) -> None:
        super().__init__(id, title, creator_id, assignee_id, due_date, BugStatus.OPEN, TaskType.BUG)
        self.severity = severity

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.creator_id} {self.assignee_id} {self.due_date} {self.severity.name}"

    @classmethod
    def from_string(cls, statement):
        parts = statement.split(" ")
        id = parts[2]
        title = parts[3]
        creator_id = parts[4]
        assignee_id = parts[5]
        due_date = get_date(parts[6])
        severity = parts[7]
        return cls(id, title, creator_id, assignee_id, due_date, severity)

    