from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid4)
    # pylint: disable=redefined-builtin
    # def __init__(self, name, id="",  description="", is_active=True) -> None:
    #     self.id = id or uuid.uuid4()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active

    #     self.validate()

    def __post_init__(self):
        self.validate()

    def __str__(self) -> str:
        return f"{self.name} - {self.description} ({self.id})"

    def __repr__(self) -> str:
        return f"<Category {self.name} ({self.id})>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Category):
            return False

        return self.id == other.id

    def update(self, name: str, description: str):
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True

        self.validate()

    def desactivate(self):
        self.is_active = False

        self.validate()

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer 255")

        if not self.name:  # len(self.name == 0):
            raise ValueError("name cannot be empty")
