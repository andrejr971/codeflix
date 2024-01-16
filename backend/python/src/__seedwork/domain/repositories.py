from abc import ABC
import abc
from dataclasses import dataclass, field
from typing import Generic, List, TypeVar
from __seedwork.domain.exceptions import NotFoundException
from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.entities import Entity

T = TypeVar('T', bound=Entity)


class RepositoryInterface(Generic[T], ABC):

    @abc.abstractmethod
    def insert(self, entity: T) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, id: str | UniqueEntityId) -> T:  # pylint: disable=redefined-builtin
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> List[T]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, entity: T) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self,  id: str | UniqueEntityId) -> None:  # pylint: disable=redefined-builtin
        raise NotImplementedError()


Input = TypeVar('Input')
Output = TypeVar('Output')


class SearchableRepositoryInterface(Generic[T, Input, Output], RepositoryInterface[T], ABC):

    @abc.abstractmethod
    def search(self, input_params: Input) -> Output:
        raise NotImplementedError()


@dataclass(slots=True)
class InMemoryRepository(RepositoryInterface[T], ABC):
    items: List[T] = field(default_factory=lambda: [])

    def insert(self, entity: T) -> None:
        self.items.append(entity)

    def find_by_id(self, id: str | UniqueEntityId) -> T:  # pylint: disable=redefined-builtin
        id_str = str(id)
        return self._get(id=id_str)

    def find_all(self) -> List[T]:
        return self.items

    def update(self, entity: T) -> None:
        entity_found = self._get(entity.id)
        index = self.items.index(entity_found)
        self.items[index] = entity

    def delete(self,  id: str | UniqueEntityId) -> None:  # pylint: disable=redefined-builtin
        id_str = str(id)
        entity_found = self._get(id=id_str)
        self.items.remove(entity_found)

    def _get(self, id: str) -> T:  # pylint: disable=redefined-builtin
        entity = next(filter(lambda i: i.id == id, self.items), None)
        if not entity:
            raise NotFoundException(f"Entity not found using ID '{id}'")
        return entity
