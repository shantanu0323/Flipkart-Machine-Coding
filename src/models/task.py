from enum import Enum

class TaskType(Enum):
    FEATURE = 1
    BUG = 2
    STORY = 3
    SUBTASK = 4

class Task:
    def __init__(self, id, title, creator_id, assignee_id, due_date, status, task_type) -> None:
        self.id = id
        self.title = title
        self.creator_id = creator_id
        self.assignee_id = assignee_id
        self.due_date = due_date
        self.status = status
        self.task_type = task_type

    def __str__(self) -> str:
        return f"{self.id} {self.title} {self.creator_id} {self.assignee_id} {self.due_date} {self.status.name} {self.task_type.name}"

