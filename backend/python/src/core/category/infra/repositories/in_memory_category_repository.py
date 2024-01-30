from uuid import UUID
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category

# pylint: disable=redefined-builtin


class InMemoryCategoryRepository(CategoryRepository):

    def __init__(self, categories: list[Category] = None):
        self.categories: list[Category] = categories or []

    def save(self, category: Category) -> None:
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category | None:
        # next((category for category in self.categories if category.id == id), None)
        for category in self.categories:
            if category.id == id:
                return category
        return None

    def delete(self, id: UUID) -> None:
        category = self.get_by_id(id)

        if category:
            self.categories.remove(category)

    def update(self, category: Category) -> None:
        old_category = self.get_by_id(id)
        if old_category:
            self.categories.remove(old_category)
            self.categories.append(category)