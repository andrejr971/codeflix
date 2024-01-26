from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):

    def __init__(self, categories=None) -> None:
        self.categories = categories or []

    def save(self, category: Category) -> None:
        self.categories.append(category)
