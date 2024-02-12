import uuid

import pytest

from src.core.category.infra.repositories.in_memory_category_repository import (
    InMemoryCategoryRepository
)
from src.core.genre.infra.repositories.in_memory_genre_repository import (
    InMemoryGenreRepository
)
from src.core.genre.domain.exceptions import RelatedCategoriesNotFound
from src.core.genre.application.usecases.create_genre import CreateGenre
from src.core.category.domain.category import Category


@pytest.fixture
def movie_category() -> Category:
    return Category(name="Movie")


@pytest.fixture
def documentary_category() -> Category:
    return Category(name="Documentary")


@pytest.fixture
def category_repository(
    movie_category,  # pylint: disable=redefined-outer-name
    documentary_category  # pylint: disable=redefined-outer-name
) -> list[Category]:
    return InMemoryCategoryRepository(
        categories=[movie_category, documentary_category]
    )


class TestCreateGenre:

    def test_create_genre_with_associated_categories(
        self,
        movie_category,  # pylint: disable=redefined-outer-name
        documentary_category,  # pylint: disable=redefined-outer-name
        category_repository  # pylint: disable=redefined-outer-name
    ):
        genre_repository = InMemoryGenreRepository()
        use_case = CreateGenre(
            repository=genre_repository,
            category_repository=category_repository
        )
        request = CreateGenre.Request(
            name="Action",
            categories={movie_category.id, documentary_category.id}
        )

        response = use_case.execute(request)

        assert isinstance(response.id, uuid.UUID)
        saved_genre = genre_repository.get_by_id(response.id)
        assert saved_genre.name == 'Action'
        assert saved_genre.categories == {
            movie_category.id, documentary_category.id
        }
        assert saved_genre.is_active

    def test_create_genre_with_inexistent_categories_raise_an_error(
        self,
        category_repository  # pylint: disable=redefined-outer-name
    ):
        genre_repository = InMemoryGenreRepository()
        use_case = CreateGenre(
            repository=genre_repository,
            category_repository=category_repository,
        )

        with pytest.raises(
            RelatedCategoriesNotFound,
            match="Categories with provided IDs not found: "
        ):
            use_case.execute(
                CreateGenre.Request(
                    name="Genre 1",
                    categories={uuid.uuid4()}
                )
            )

        assert len(genre_repository.list()) == 0

    def test_create_genre_without_categories(
        self,
        category_repository  # pylint: disable=redefined-outer-name
    ):
        genre_repository = InMemoryGenreRepository()

        use_case = CreateGenre(
            repository=genre_repository,
            category_repository=category_repository,
        )

        output = use_case.execute(
            CreateGenre.Request(
                name="Genre 1",
            )
        )

        assert len(genre_repository.list()) == 1
        created_genre = genre_repository.get_by_id(output.id)
        assert created_genre.name == "Genre 1"
        assert created_genre.categories == set()
        assert created_genre.is_active
