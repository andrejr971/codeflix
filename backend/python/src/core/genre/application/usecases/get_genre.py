
from dataclasses import dataclass
from uuid import UUID
from src.core.genre.domain.exceptions import GenreNotFound

from src.core.genre.domain.genre_repository import GenreRepository


class GetGenre:
    def __init__(self, repository: GenreRepository) -> None:
        self.repository = repository

    @dataclass
    class Request:
        id: UUID

    @dataclass
    class Response:
        id: UUID
        name: str
        categories: list[UUID]
        is_active: bool

    def execute(self, request: Request) -> Response:
        genre = self.repository.get_by_id(id=request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        return self.Response(
            id=genre.id,
            name=genre.name,
            categories=genre.categories,
            is_active=genre.is_active
        )
