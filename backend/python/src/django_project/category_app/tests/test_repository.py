import pytest
from src.core.category.domain.category import Category
from src.django_project.category_app.repository import DjangoORMCategoryRepository
from src.django_project.category_app.models import Category as CategoryModel

# pylint: disable=no-member


@pytest.mark.django_db
class TestSave:
    def test_save_category_in_database(self):
        category = Category(
            name="Category",
            description="Description",
            is_active=True
        )

        repository = DjangoORMCategoryRepository()
        assert CategoryModel.objects.count() == 0

        repository.save(category)
        assert CategoryModel.objects.count() == 1
