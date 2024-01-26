from unittest.mock import create_autospec

from src.core.category.application.category_repository import CategoryRepository

# pylint: disable=line-too-long
from src.core.category.application.usecases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category


class TestGetCategory:

    def test_return_found_category(self):
        category = Category(name="Film", description="some description")
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = GetCategory(repository=mock_repository)

        request = GetCategoryRequest(
            id=category.id
        )
        response = use_case.execute(request)

        assert response is not None
        assert response == GetCategoryResponse(
            id=category.id,
            description=category.description,
            is_active=category.is_active,
            name=category.name,
        )
