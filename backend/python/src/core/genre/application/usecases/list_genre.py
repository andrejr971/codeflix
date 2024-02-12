from dataclasses import dataclass

from _pytest.pathlib import uuid
from src.core.genre.domain.genre_repository import GenreRepository


@dataclass
class ResponseListGenre:
    id: uuid.UUID
    name: str
    categories: list[uuid.UUID]
    is_active: bool


class ListGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Request:
        pass

    @dataclass
    class Response:
        data: list[ResponseListGenre]

    def execute(self, request: Request) -> Response:
        genres = self.repository.list()

        mapped_genres = [
            ResponseListGenre(
                id=genre.id,
                name=genre.name,
                categories=genre.categories,
                is_active=genre.is_active
            )
            for genre in genres
        ]

        return self.Response(data=mapped_genres)
