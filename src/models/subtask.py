from enum import Enum
from models.story_task import StoryTask

class SubtaskStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    COMPLETED = 3

class SubTask(StoryTask):
    def __init__(self, id, parent_id, title, status) -> None:
        self.id = id
        self.parent_id = parent_id
        self.title = title
        self.status = status

    def __str__(self) -> str:
        return f"{self.id} {self.parent_id} {self.title} {self.status}"


