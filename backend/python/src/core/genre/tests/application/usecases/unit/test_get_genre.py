from unittest.mock import create_autospec
import uuid

import pytest

from src.core.genre.application.usecases.get_genre import GetGenre
from src.core.genre.domain.exceptions import GenreNotFound

from src.core.genre.domain.genre import Genre
from src.core.genre.domain.genre_repository import GenreRepository


class TestGetGenre:

    def test_return_found_genre(self):

        mock_genre = Genre(
            id=uuid.uuid4(),
            name="Drama",
            is_active=True,
        )
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = mock_genre

        use_case = GetGenre(repository=mock_repository)
        request = GetGenre.Request(id=mock_genre.id)

        response = use_case.execute(request)

        assert response == GetGenre.Response(
            id=mock_genre.id,
            name="Drama",
            is_active=True,
            categories=set(),
        )

    def test_when_category_not_found_then_raise_exception(self):
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = None

        use_case = GetGenre(repository=mock_repository)
        request = GetGenre.Request(id=uuid.uuid4())

        with pytest.raises(GenreNotFound):
            use_case.execute(request)
