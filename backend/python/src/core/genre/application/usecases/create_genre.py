from dataclasses import dataclass, field

from uuid import UUID

from src.core.genre.domain.genre import Genre
from src.core.genre.domain.exceptions import InvalidGenre, RelatedCategoriesNotFound
from src.core.category.domain.category_repository import CategoryRepository
from src.core.genre.domain.genre_repository import GenreRepository


class CreateGenre:
    def __init__(
        self,
        repository: GenreRepository,
        category_repository: CategoryRepository
    ) -> None:
        self.repository = repository
        self.category_repository = category_repository

    @dataclass
    class Request:
        name: str
        categories: set[UUID] = field(default_factory=set)
        is_active: bool = True

    @dataclass
    class Response:
        id: UUID

    def execute(self, request: Request) -> Response:
        categories = {
            category.id for category in self.category_repository.list()
        }

        if not request.categories.issubset(categories):
            raise RelatedCategoriesNotFound(
                f"Categories with provided IDs not found: {request.categories - categories}"
            )

        try:
            genre = Genre(
                name=request.name,
                categories=request.categories,
                is_active=request.is_active
            )
        except ValueError as error:
            raise InvalidGenre(error) from error

        self.repository.save(genre)
        return self.Response(id=genre.id)
