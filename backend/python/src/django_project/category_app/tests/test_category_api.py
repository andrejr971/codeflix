import uuid
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.test import APIClient
from src.core.category.domain.category import Category

from src.django_project.category_app.repository import DjangoORMCategoryRepository

# Create your tests here.

# pylint: disable=no-method-argument


class BaseTestMock:
    @pytest.fixture
    def category_movie(self) -> Category:
        return Category(
            name="Movie",
            description="Category 1 description"
        )

    @pytest.fixture
    def category_documentary(self) -> Category:
        return Category(
            name="Documentary",
            description="Category 2 description"
        )

    @pytest.fixture
    def repository(self) -> DjangoORMCategoryRepository:
        return DjangoORMCategoryRepository()


@pytest.mark.django_db
class TestCategoryAPI(BaseTestMock):

    def test_list_categories(
        self,
        category_documentary: Category,
        category_movie: Category,
        repository: DjangoORMCategoryRepository
    ) -> None:
        repository.save(category_movie)
        repository.save(category_documentary)

        url = '/api/categories/'
        response = APIClient().get(url)

        expect_data = [{
            "id": str(category_movie.id),
            "name": category_movie.name,
            "description": category_movie.description,
            "is_active": category_movie.is_active
        }, {
            "id": str(category_documentary.id),
            "name": category_documentary.name,
            "description": category_documentary.description,
            "is_active": category_documentary.is_active
        }]

        assert response.status_code == HTTP_200_OK
        assert len(response.data) == 2
        assert response.data == expect_data


@pytest.mark.django_db
class TestRetrieveAPI(BaseTestMock):

    def test_when_id_is_invalid_return_400(self) -> None:
        url = '/api/categories/invalid_id/'
        response = APIClient().get(url)

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_return_category_when_exists(
        self,
        category_documentary: Category,
        category_movie: Category,
        repository: DjangoORMCategoryRepository
    ) -> None:
        repository.save(category_movie)
        repository.save(category_documentary)

        url = f'/api/categories/{category_documentary.id}/'
        response = APIClient().get(url)

        expect_data = {
            "id": str(category_documentary.id),
            "name": category_documentary.name,
            "description": category_documentary.description,
            "is_active": category_documentary.is_active
        }

        assert response.status_code == HTTP_200_OK
        assert response.data == expect_data

    def test_return_404_when_not_exists(self):
        invalid_uuid = uuid.uuid4()
        url = f'/api/categories/{invalid_uuid}/'
        response = APIClient().get(url)

        assert response.status_code == HTTP_404_NOT_FOUND
