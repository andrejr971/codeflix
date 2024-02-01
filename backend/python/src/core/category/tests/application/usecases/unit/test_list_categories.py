from unittest.mock import create_autospec
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.usecases.list_categories import CategoryOutput, ListCategories, ListCategoriesRequest, ListCategoriesResponse
from src.core.category.domain.category import Category


class TestListCategories:
    def test_when_no_categories_should_return_empty_list(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = []

        use_case = ListCategories(repository=mock_repository)
        request = ListCategoriesRequest()

        response = use_case.execute(request)

        assert response == ListCategoriesResponse(
            data=[]
        )

    def test_when_no_categories_should_return_list(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes",
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = [category]

        use_case = ListCategories(repository=mock_repository)
        request = ListCategoriesRequest()

        response = use_case.execute(request)

        assert response == ListCategoriesResponse(
            data=[
                CategoryOutput(
                    id=category.id,
                    name=category.name,
                    description=category.description,
                    is_active=category.is_active,
                )
            ]
        )
