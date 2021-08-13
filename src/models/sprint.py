class Sprint:
    def __init__(self, id, name, tasks=None) -> None:
        self.id = id
        self.name = name
        self.tasks = tasks

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tasks}"

    @classmethod
    def from_string(cls, statement):
        parts = statement.split(" ")
        id = parts[2]
        name = parts[3]
        return cls(id, name)


        