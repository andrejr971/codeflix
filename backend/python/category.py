import uuid


class Category:
    # pylint: disable=redefined-builtin
    def __init__(self, name, id="",  description="", is_active=True) -> None:
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.is_active = is_active

        self.validate()

    def __str__(self) -> str:
        return f"{self.name} - {self.description} ({self.id})"

    def __repr__(self) -> str:
        return f"<Category {self.name} ({self.id})>"

    def update(self, name: str, description: str):
        self.name = name
        self.description = description

        self.validate()

    def actived(self):
        self.is_active = True

    def desactived(self):
        self.is_active = False

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer 255")

        if not self.name:  # len(self.name == 0):
            raise ValueError("name cannot empty")
