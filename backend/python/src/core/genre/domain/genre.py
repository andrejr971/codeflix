from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Genre:
    name: str
    is_active: bool = True
    categories: set[UUID] = field(default_factory=set)
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        self.validate()

    def __str__(self) -> str:
        return f"{self.name} ({self.id})"

    def __repr__(self) -> str:
        return f"<Genre {self.name} ({self.id})>"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Genre):
            return False

        return self.id == other.id

    def change_name(self, name: str):
        self.name = name
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

        if not self.name:
            raise ValueError("name cannot be empty")

    def add_category(self, category_id: UUID):
        self.categories.add(category_id)
        self.validate()

    def remove_category(self, category_id: UUID):
        self.categories.remove(category_id)
        self.validate()
