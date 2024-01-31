from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK

# Create your tests here.


class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        url = '/api/categories/'
        response = self.client.get(url)

        expect_data = [
            {
                "id": 1,
                "name": "Category 1",
                "description": "Category 1 description",
                "is_active": True,
            },
            {
                "id": 2,
                "name": "Category 2",
                "description": "Category 2 description",
                "is_active": True,
            },
            {
                "id": 3,
                "name": "Category 3",
                "description": "Category 3 description",
                "is_active": True,
            },
        ]

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expect_data)
