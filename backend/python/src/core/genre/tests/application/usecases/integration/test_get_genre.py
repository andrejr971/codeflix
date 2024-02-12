# pylint: disable=line-too-long
from uuid import uuid4

import pytest
from src.core.genre.application.usecases.get_genre import GetGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.domain.exceptions import GenreNotFound
from src.core.genre.infra.repositories.in_memory_genre_repository import InMemoryGenreRepository


class TestGetGenre:

    def test_get_genre_by_id(self):
        genre = Genre(name="Drama")

        repository = InMemoryGenreRepository(
            genres=[genre]
        )

        assert len(repository.genres) == 1

        use_case = GetGenre(repository=repository)
        request = GetGenre.Request(
            id=genre.id
        )

        response = use_case.execute(request)

        assert response == GetGenre.Response(
            id=genre.id,
            name="Drama",
            categories=set(),
            is_active=True
        )

    def test_genre_non_exists(self):
        genre = Genre(name="Drama")

        repository = InMemoryGenreRepository(
            genres=[genre]
        )

        use_case = GetGenre(repository=repository)
        id_not_found = uuid4()
        request = GetGenre.Request(
            id=id_not_found
        )

        with pytest.raises(GenreNotFound) as error:
            use_case.execute(request)

        assert str(error.value) == f"Genre with {id_not_found} not found"
