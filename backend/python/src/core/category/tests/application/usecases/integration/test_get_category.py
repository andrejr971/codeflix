# pylint: disable=line-too-long
from uuid import uuid4

import pytest
from src.core.category.application.usecases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.domain.exceptions import CategoryNotFound
from src.core.category.infra.repositories.in_memory_category_repository import InMemoryCategoryRepository


class TestGetCategory:

    def test_get_category_by_id(self):
        category_film = Category(name="Film", description="some description")
        category_serie = Category(name="Serie", description="some description")

        repository = InMemoryCategoryRepository(
            categories=[category_film, category_serie]
        )

        assert len(repository.categories) == 2

        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(
            id=category_film.id
        )

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id=category_film.id,
            name="Film",
            description="some description",
            is_active=True
        )

    def test_category_non_exists(self):
        category_film = Category(name="Film", description="some description")
        category_serie = Category(name="Serie", description="some description")

        repository = InMemoryCategoryRepository(
            categories=[category_film, category_serie]
        )

        use_case = GetCategory(repository=repository)
        id_not_found = uuid4()
        request = GetCategoryRequest(
            id=id_not_found
        )

        with pytest.raises(CategoryNotFound) as error:
            use_case.execute(request)

        assert str(error.value) == f"Category with {id_not_found} not found"
