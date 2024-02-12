from unittest.mock import create_autospec
import uuid

import pytest
from src.core.category.domain.category import Category
from src.core.category.domain.category_repository import CategoryRepository
from src.core.genre.application.usecases.update_genre import UpdateGenre
from src.core.genre.domain.exceptions import GenreNotFound, InvalidGenre, RelatedCategoriesNotFound
from src.core.genre.domain.genre import Genre

from src.core.genre.domain.genre_repository import GenreRepository


class BaseTestMock:
    @pytest.fixture
    def mock_genre_repository(self) -> GenreRepository:
        return create_autospec(GenreRepository)

    @pytest.fixture
    def mock_repository_genre(self):
        genre = Genre(
            name="Action",
            is_active=True
        )
        repository = create_autospec(GenreRepository)
        repository.get_by_id.return_value = genre

        return {
            "repository": repository,
            "genre": genre
        }

    @pytest.fixture
    def movie_category(self) -> Category:
        return Category(name="Movie")

    @pytest.fixture
    def documentary_category(self) -> Category:
        return Category(name="Documentary")

    @pytest.fixture
    def mock_category_repository_with_categories(
        self,
        movie_category,
        documentary_category
    ) -> CategoryRepository:
        repository = create_autospec(CategoryRepository)
        repository.list.return_value = [movie_category, documentary_category]
        return repository

    @pytest.fixture
    def mock_empty_category_repository(self) -> CategoryRepository:
        repository = create_autospec(CategoryRepository)
        repository.list.return_value = []
        return repository


class TestUpdateGenre(BaseTestMock):

    def test_not_update_genre_when_genre_not_exists(
        self,
        mock_genre_repository,
        mock_category_repository_with_categories
    ):
        use_case = UpdateGenre(
            repository=mock_genre_repository,
            category_repository=mock_category_repository_with_categories
        )

        request = UpdateGenre.Request(id=uuid.uuid4())
        mock_genre_repository.get_by_id.return_value = None

        with pytest.raises(GenreNotFound, match='Genre with .* not found'):
            use_case.execute(request=request)

    def test_when_categories_do_not_exist_then_raise_related_not_found(
        self,
        mock_empty_category_repository,
        mock_genre_repository
    ):
        genre = Genre(
            name="Action",
            is_active=True
        )
        repository = mock_genre_repository
        repository.get_by_id.return_value = genre

        use_case = UpdateGenre(
            repository=repository,
            category_repository=mock_empty_category_repository
        )
        category_id = uuid.uuid4()
        request = UpdateGenre.Request(
            id=genre.id,
            categories={category_id}
        )

        with pytest.raises(RelatedCategoriesNotFound) as error:
            use_case.execute(request)

        assert str(category_id) in str(error.value)

    def test_when_created_genre_is_invalid_then_raise_invalid_genre(
        self,
        movie_category,
        mock_category_repository_with_categories,
        mock_repository_genre
    ):
        repository = mock_repository_genre["repository"]
        genre = mock_repository_genre["genre"]

        use_case = UpdateGenre(
            repository=repository,
            category_repository=mock_category_repository_with_categories
        )
        request = UpdateGenre.Request(
            id=genre.id,
            name="",
            categories={movie_category.id}
        )
        with pytest.raises(InvalidGenre, match="name cannot be empty"):
            use_case.execute(request)

    def test_update_name(
        self,
        mock_repository_genre
    ):
        repository = mock_repository_genre["repository"]
        genre = mock_repository_genre["genre"]

        use_case = UpdateGenre(
            repository=repository,
            category_repository=create_autospec(CategoryRepository)
        )
        request = UpdateGenre.Request(
            id=genre.id,
            name="Adventure"
        )

        use_case.execute(request)
        assert genre.name == "Adventure"
        repository.update.assert_called_once_with(genre)

    def test_can_desactive_and_active_genre(
        self,
        mock_repository_genre,
    ):
        repository = mock_repository_genre["repository"]
        genre = mock_repository_genre["genre"]

        use_case = UpdateGenre(
            repository=repository,
            category_repository=create_autospec(CategoryRepository)
        )
        request = UpdateGenre.Request(
            id=genre.id,
            is_active=False
        )

        use_case.execute(request=request)

        assert genre.is_active is False
        repository.update.assert_called_once_with(genre)

        request = UpdateGenre.Request(
            id=genre.id,
            is_active=True
        )

        use_case.execute(request=request)

        assert genre.is_active is True

    def test_update_categories_in_genre(
        self,
        mock_repository_genre,
        mock_category_repository_with_categories,
        movie_category,
        documentary_category
    ):
        repository = mock_repository_genre["repository"]
        genre = mock_repository_genre["genre"]

        assert len(genre.categories) == 0

        use_case = UpdateGenre(
            repository=repository,
            category_repository=mock_category_repository_with_categories
        )
        request = UpdateGenre.Request(
            id=genre.id,
            categories={documentary_category.id}
        )

        use_case.execute(request)
        assert len(genre.categories) == 1

        request = UpdateGenre.Request(
            id=genre.id,
            categories={documentary_category.id, movie_category.id}
        )

        use_case.execute(request)
        assert len(genre.categories) == 2
