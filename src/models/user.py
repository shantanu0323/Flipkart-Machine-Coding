class User:
    def __init__(self, id, name, email) -> None:
        self.id = id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        print(f"User: {self.id} {self.name} {self.email}")

    @classmethod
    def from_string(cls, statement):
        parts = statement.split(" ")
        id = parts[2]
        name = parts[3]
        email = parts[4]
        return cls(id, name, email)

    # TODO: create method for auto generation of id