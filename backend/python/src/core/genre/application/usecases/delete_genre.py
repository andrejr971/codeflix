from dataclasses import dataclass
from uuid import UUID
from src.core.genre.domain.exceptions import GenreNotFound

from src.core.genre.domain.genre_repository import GenreRepository


class DeleteGenre:

    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Request:
        id: UUID

    def execute(self, request=Request) -> None:
        genre = self.repository.get_by_id(request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        self.repository.delete(genre.id)
