from uuid import UUID

import pytest

# pylint: disable=line-too-long
from src.core.category.application.usecases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.domain.exceptions import InvalidCategoryData
from src.core.category.infra.repositories.in_memory_category_repository import InMemoryCategoryRepository


class TestCreateCategory:

    def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(repository=repository)

        request = CreateCategoryRequest(
            name="Movie",
            description="some description",
            is_active=True
        )

        response = use_case.execute(request)

        assert response is not None
        assert isinstance(response.id, UUID)
        assert len(repository.categories) == 1

        persisted_category = repository.categories[0]
        assert persisted_category.id == response.id
        assert persisted_category.name == "Movie"
        assert persisted_category.description == "some description"
        assert persisted_category.is_active

    def test_not_be_able_create_category(self):
        repository = InMemoryCategoryRepository()
        use_case = CreateCategory(repository=repository)

        with pytest.raises(InvalidCategoryData) as error:
            request = CreateCategoryRequest(
                name="",
            )

            use_case.execute(request)

        assert str(error.value) == 'name cannot be empty'
        assert len(repository.categories) == 0
