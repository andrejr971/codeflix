from abc import ABC, abstractmethod
from uuid import UUID
from src.core.category.domain.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    def save(self, category: Category) -> None:
        raise NotImplementedError

    @abstractmethod
    # pylint: disable=redefined-builtin
    def get_by_id(self, id: UUID) -> Category:
        raise NotImplementedError
