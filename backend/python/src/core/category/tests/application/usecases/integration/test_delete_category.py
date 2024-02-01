import uuid
from src.core.category.application.usecases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.repositories.in_memory_category_repository import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category_moviee = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        category_serie = Category(
            id=uuid.uuid4(),
            name="Série",
            description="Categoria para séries",
            is_active=True,
        )
        repository = InMemoryCategoryRepository(
            categories=[
                category_moviee,
                category_serie,
            ]
        )

        use_case = DeleteCategory(repository=repository)
        request = DeleteCategoryRequest(id=category_moviee.id)

        assert repository.get_by_id(category_moviee.id) is not None
        response = use_case.execute(request)

        assert repository.get_by_id(category_moviee.id) is None
        assert response is None
