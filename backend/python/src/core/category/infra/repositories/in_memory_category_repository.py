from uuid import UUID
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):

    def __init__(self, categories=None) -> None:
        self.categories = categories or []

    def save(self, category: Category) -> None:
        self.categories.append(category)

    # pylint: disable=redefined-builtin
    def get_by_id(self, id: UUID) -> Category | None:
        # next((category for category in self.categories if category.id == id), None)
        for category in self.categories:
            if category.id == id:
                return category
        return None
