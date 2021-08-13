from enum import Enum
from models.task import Task
from models.task import TaskType
from services.utils import get_date

class StoryStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class StoryTask(Task):
    def __init__(self, id, title, creator_id, assignee_id, due_date, summary, sprint=None, subtasks=None) -> None:
        super().__init__(id, title, creator_id, assignee_id, due_date, StoryStatus.OPEN, TaskType.STORY)
        self.summary = summary
        self.sprint = sprint
        self.subtasks = subtasks

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.creator_id} {self.assignee_id} {self.due_date} {self.summary} {self.sprint}"


    def create_subtask(self, id, title, status):
        from models.subtask import SubTask
        self.subtasks.append(SubTask(id, self.id, title, status))

    @classmethod
    def from_string(cls, statement):
        parts = statement.split(" ")
        id = parts[2]
        title = parts[3]
        creator_id = parts[4]
        assignee_id = parts[5]
        due_date = get_date(parts[6])
        summary = parts[7]
        sprint = parts[8] if len(parts) == 9 else None
        return cls(id, title, creator_id, assignee_id, due_date, summary, sprint)

