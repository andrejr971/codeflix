from src.core.category.domain.category import Category
from src.core.category.application.usecases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.infra.repositories.in_memory_category_repository import InMemoryCategoryRepository


class TestUpdateCategory:
    def test_can_update_category_name_and_description(self):
        category = Category(
            name="Movie",
            description="some description",
        )
        repository = InMemoryCategoryRepository()
        repository.save(category=category)

        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="Serie",
            description="some description 1"
        )
        use_case.execute(request=request)

        updated_category = repository.get_by_id(category.id)
        assert updated_category.name == "Serie"
        assert updated_category.description == "some description 1"
