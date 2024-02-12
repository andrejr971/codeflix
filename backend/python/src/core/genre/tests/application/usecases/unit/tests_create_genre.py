from unittest.mock import create_autospec
import uuid

import pytest


from src.core.genre.domain.genre import Genre
from src.core.genre.domain.exceptions import InvalidGenre, RelatedCategoriesNotFound
from src.core.genre.application.usecases.create_genre import CreateGenre
from src.core.genre.domain.genre_repository import GenreRepository
from src.core.category.domain.category import Category
from src.core.category.domain.category_repository import CategoryRepository


class BaseTestMock:
    @pytest.fixture
    def mock_genre_repository(self) -> GenreRepository:
        return create_autospec(GenreRepository)

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


class TestCreateGenre(BaseTestMock):

    def test_when_categories_do_not_exist_then_raise_related_not_found(
        self,
        mock_empty_category_repository,
        mock_genre_repository
    ):
        use_case = CreateGenre(
            repository=mock_genre_repository,
            category_repository=mock_empty_category_repository
        )
        category_id = uuid.uuid4()
        request = CreateGenre.Request(name="Action", categories={category_id})

        with pytest.raises(RelatedCategoriesNotFound) as error:
            use_case.execute(request)

        assert str(category_id) in str(error.value)

    def test_when_created_genre_is_invalid_then_raise_invalid_genre(
        self,
        movie_category,
        mock_category_repository_with_categories,
        mock_genre_repository
    ):
        use_case = CreateGenre(
            repository=mock_genre_repository,
            category_repository=mock_category_repository_with_categories
        )
        request = CreateGenre.Request(name="", categories={movie_category.id})
        with pytest.raises(InvalidGenre, match="name cannot be empty"):
            use_case.execute(request)

    def test_when_created_genre_is_valid_and_categories_exist_then_save_genre(
        self,
        documentary_category,
        movie_category,
        mock_category_repository_with_categories,
        mock_genre_repository,
    ):
        use_case = CreateGenre(
            repository=mock_genre_repository,
            category_repository=mock_category_repository_with_categories,
        )

        output = use_case.execute(
            CreateGenre.Request(
                name="Romance",
                categories={documentary_category.id, movie_category.id},
            )
        )

        assert output == CreateGenre.Response(id=output.id)
        mock_genre_repository.save.assert_called_once_with(
            Genre(
                id=output.id,
                name="Romance",
                is_active=True,
                categories={documentary_category.id, movie_category.id},
            )
        )

    def test_create_genre_without_categories(
        self,
        mock_category_repository_with_categories,
        mock_genre_repository,
    ):
        use_case = CreateGenre(
            repository=mock_genre_repository,
            category_repository=mock_category_repository_with_categories,
        )

        output = use_case.execute(
            CreateGenre.Request(
                name="Romance",
            )
        )

        assert output == CreateGenre.Response(id=output.id)
        mock_genre_repository.save.assert_called_once_with(
            Genre(
                id=output.id,
                name="Romance",
                is_active=True,
            )
        )
