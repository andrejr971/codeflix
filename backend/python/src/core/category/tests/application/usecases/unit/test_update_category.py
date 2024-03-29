from unittest.mock import create_autospec
import uuid
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.usecases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="Movie"
        )

        use_case.execute(request=request)

        assert category.name == "Movie"
        assert category.description == "Categoria para filmes"
        mock_repository.update.assert_called_once_with(category)

    def test_update_category_description(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            description="Some description"
        )

        use_case.execute(request=request)
        print(category)

        assert category.name == "Filme"
        assert category.description == "Some description"
        mock_repository.update.assert_called_once_with(category)

    def test_can_desactive_category(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=False
        )

        use_case.execute(request=request)
        print(category)

        assert category.name == "Filme"
        assert category.is_active is False
        mock_repository.update.assert_called_once_with(category)

    def test_can_active_category(self):
        category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=False,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=True
        )

        use_case.execute(request=request)
        print(category)

        assert category.name == "Filme"
        assert category.is_active is True
        mock_repository.update.assert_called_once_with(category)
