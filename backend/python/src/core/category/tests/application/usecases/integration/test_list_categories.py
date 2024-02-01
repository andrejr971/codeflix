from src.core.category.application.usecases.list_categories import CategoryOutput, ListCategories, ListCategoriesRequest, ListCategoriesResponse
from src.core.category.infra.repositories.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.domain.category import Category


class TestListCategories:
    def test_return_empty_list(self):
        repository = InMemoryCategoryRepository()

        use_case = ListCategories(repository=repository)
        request = ListCategoriesRequest()

        response = use_case.execute(request)

        assert response == ListCategoriesResponse(
            data=[]
        )

    def test_return_list(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes",
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = ListCategories(repository=repository)
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
