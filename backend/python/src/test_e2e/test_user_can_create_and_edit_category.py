import pytest

from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateAndeEditCategory:
    def test_user_can_create_category(self,):
        client = APIClient()

        # verify empty list
        list_response = client.get('/api/categories/')
        assert list_response.data == {"data": []}

        # create category
        create_response = client.post(
            '/api/categories/',
            data={
                "name": "Movie",
                "description": "Test Description"
            }
        )
        assert create_response.status_code == 201
        created_category_id = create_response.data["id"]

        # Verify category created in list
        list_response = client.get('/api/categories/')
        assert list_response.data == {
            "data": [
                {
                    "id": created_category_id,
                    "name": "Movie",
                    "description": "Test Description",
                    "is_active": True
                }
            ]
        }

        # Edit category
        edit_response = client.put(
            f'/api/categories/{created_category_id}/',
            data={
                "name": "Serie",
                "description": "Test Description Updated",
                "is_active": True
            }
        )
        assert edit_response.status_code == 204

        # Verify category edited in list
        list_response = client.get('/api/categories/')
        assert list_response.data == {
            "data": [
                {
                    "id": created_category_id,
                    "name": "Serie",
                    "description": "Test Description Updated",
                    "is_active": True
                }
            ]
        }

        # Delete category
        delete_response = client.delete(
            f'/api/categories/{created_category_id}/'
        )
        assert delete_response.status_code == 204

        # Verify category deleted in list
        list_response = client.get('/api/categories/')
        assert list_response.data == {"data": []}
