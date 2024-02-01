from unittest.mock import create_autospec
import uuid

import pytest

from src.core.category.domain.category_repository import CategoryRepository

# pylint: disable=line-too-long
from src.core.category.application.usecases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.domain.exceptions import CategoryNotFound


class TestGetCategory:

    def test_return_found_category(self):
        mock_category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = mock_category

        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(id=mock_category.id)

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id=mock_category.id,
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

    def test_when_category_not_found_then_raise_exception(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(id=uuid.uuid4())

        with pytest.raises(CategoryNotFound):
            use_case.execute(request)
