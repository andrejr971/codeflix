import uuid
import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
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
class TestListAPI(BaseTestMock):

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

        expect_data = {
            "data": [
                {
                    "id": str(category_movie.id),
                    "name": category_movie.name,
                    "description": category_movie.description,
                    "is_active": category_movie.is_active
                },
                {
                    "id": str(category_documentary.id),
                    "name": category_documentary.name,
                    "description": category_documentary.description,
                    "is_active": category_documentary.is_active
                }
            ]
        }

        assert response.status_code == HTTP_200_OK
        assert len(response.data['data']) == 2
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
            "data": {
                "id": str(category_documentary.id),
                "name": category_documentary.name,
                "description": category_documentary.description,
                "is_active": category_documentary.is_active
            }
        }

        assert response.status_code == HTTP_200_OK
        assert response.data == expect_data

    def test_return_404_when_not_exists(self):
        invalid_uuid = uuid.uuid4()
        url = f'/api/categories/{invalid_uuid}/'
        response = APIClient().get(url)

        assert response.status_code == HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestCreateAPI(BaseTestMock):

    def test_when_payload_is_invalid_return_400(self) -> None:
        url = '/api/categories/'
        response = APIClient().post(
            url,
            data={
                "name": "",
                "description": "some description"
            }
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data == {"name": ["This field may not be blank."]}

    def test_wheh_payload_is_valid_return_200(
        self,
        category_movie: Category,
        repository: DjangoORMCategoryRepository
    ) -> None:
        url = '/api/categories/'
        response = APIClient().post(
            url,
            data={
                "name": category_movie.name,
                "description": category_movie.description,
                "is_active": category_movie.is_active
            }
        )

        assert response.status_code == HTTP_201_CREATED
        assert response.data["id"]

        assert repository.get_by_id(
            uuid.UUID(response.data["id"])
        ).name == category_movie.name


@pytest.mark.django_db
class TestUpdateAPI(BaseTestMock):

    def test_when_payload_is_invalid_return_400(self) -> None:
        url = '/api/categories/invalid_id/'
        response = APIClient().put(
            url,
            data={
                "name": "",
                "description": "some description",
            },
        )

        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.data == {
            "name": ["This field may not be blank."],
            "id": ["Must be a valid UUID."],
            "is_active": ["This field is required."],
        }

    def test_when_payload_is_valid_return_204(self) -> None:
        category = Category(
            name="Movie",
            description="Category 1 description"
        )

        repository = DjangoORMCategoryRepository()
        repository.save(category)

        url = f'/api/categories/{category.id}/'
        response = APIClient().put(
            url,
            data={
                "name": "Documentary",
                "description": "New description",
                "is_active": True
            }
        )

        updated_category = repository.get_by_id(category.id)

        assert response.status_code == HTTP_204_NO_CONTENT
        assert updated_category.name == "Documentary"
        assert updated_category.description == "New description"
        assert updated_category.is_active

    def test_when_category_does_not_exist_then_return_404(
        self,
    ) -> None:
        url = f'/api/categories/{uuid.uuid4()}/'
        response = APIClient().put(
            url,
            data={
                "name": "Documentary",
                "description": "New description",
                "is_active": True
            }
        )

        assert response.status_code == HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestDeleteAPI(BaseTestMock):

    def test_when_id_is_invalid_return_400(self) -> None:
        url = '/api/categories/invalid_id/'
        response = APIClient().delete(url)

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_when_id_is_valid_return_404(self) -> None:
        url = f'/api/categories/{uuid.uuid4()}/'
        response = APIClient().delete(url)

        assert response.status_code == HTTP_404_NOT_FOUND

    def test_when_id_is_valid_return_204(
        self,
        category_movie: Category,
        repository: DjangoORMCategoryRepository
    ) -> None:
        repository.save(category_movie)

        url = f'/api/categories/{category_movie.id}/'
        response = APIClient().delete(url)

        assert response.status_code == HTTP_204_NO_CONTENT
        assert not repository.get_by_id(category_movie.id)
        assert repository.list() == []


@pytest.mark.django_db
class TestPatchAPI(BaseTestMock):

    def test_when_id_is_invalid_return_400(self) -> None:
        url = '/api/categories/invalid_id/'
        response = APIClient().patch(url, data={})

        assert response.status_code == HTTP_400_BAD_REQUEST

    def test_when_id_is_valid_return_404(self) -> None:
        url = f'/api/categories/{uuid.uuid4()}/'
        response = APIClient().patch(url, data={})

        assert response.status_code == HTTP_404_NOT_FOUND

    def test_when_payload_is_valid_return_204(self) -> None:
        category = Category(
            name="Movie",
            description="Category 1 description"
        )

        repository = DjangoORMCategoryRepository()
        repository.save(category)

        url = f'/api/categories/{category.id}/'
        response = APIClient().patch(
            url,
            data={
                "name": "Documentary",
            }
        )

        updated_category = repository.get_by_id(category.id)

        assert response.status_code == HTTP_204_NO_CONTENT
        assert updated_category.name == "Documentary"
        assert updated_category.description == "Category 1 description"
        assert updated_category.is_active

        response = APIClient().patch(
            url,
            data={
                "description": "New description",
            }
        )

        updated_category = repository.get_by_id(category.id)
        assert updated_category.name == "Documentary"
        assert updated_category.description == "New description"

        response = APIClient().patch(
            url,
            data={
                "is_active": False,
            }
        )

        updated_category = repository.get_by_id(category.id)
        assert updated_category.name == "Documentary"
        assert updated_category.description == "New description"
        assert not updated_category.is_active
