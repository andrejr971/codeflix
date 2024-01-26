from unittest.mock import MagicMock
from uuid import UUID

import pytest
from src.core.category.application.category_repository import CategoryRepository

# pylint: disable=line-too-long
from src.core.category.application.usecases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.domain.exceptions import InvalidCategoryData


class TestCreateCategory:

    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)

        request = CreateCategoryRequest(
            name="Film",
            description="some description",
            is_active=True
        )

        category_id = use_case.execute(request)

        assert category_id is not None
        assert isinstance(category_id, UUID)
        assert mock_repository.save.called is True

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            request = CreateCategoryRequest(
                name="",
            )

            use_case.execute(request)

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == 'name cannot be empty'
        assert mock_repository.save.called is False
