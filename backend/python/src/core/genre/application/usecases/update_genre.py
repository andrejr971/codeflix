from dataclasses import dataclass
from uuid import UUID

from src.core.category.domain.category_repository import CategoryRepository
from src.core.genre.domain.exceptions import GenreNotFound, InvalidGenre, RelatedCategoriesNotFound
from src.core.genre.domain.genre_repository import GenreRepository


class UpdateGenre:

    def __init__(self, repository: GenreRepository, category_repository: CategoryRepository):
        self.repository = repository
        self.category_repository = category_repository

    @dataclass
    class Request:
        id: UUID
        name: str | None = None
        categories: set[UUID] | None = None
        is_active: bool | None = None

    def execute(self, request=Request) -> None:
        genre = self.repository.get_by_id(request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        categories = {
            category.id for category in self.category_repository.list()
        }

        try:
            if request.name is not None:
                genre.change_name(name=request.name)

            if request.is_active is True:
                genre.activate()

            if request.is_active is False:
                genre.desactivate()

            if request.categories is not None:
                if not request.categories.issubset(categories):
                    raise RelatedCategoriesNotFound(
                        f"Categories with provided IDs not found: {request.categories - categories}"
                    )

                if len(genre.categories) > 0:
                    categories_copy = genre.categories.copy()
                    for category_id in categories_copy:
                        genre.remove_category(category_id)

                for category_id in request.categories:
                    genre.add_category(category_id)

        except ValueError as error:
            raise InvalidGenre(error) from error

        self.repository.update(genre)
