# from django.shortcuts import render
from uuid import UUID
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from src.core.category.application.usecases.get_category import GetCategory, GetCategoryRequest

from src.core.category.application.usecases.list_categories import ListCategories, ListCategoriesRequest
from src.core.category.domain.exceptions import CategoryNotFound
from src.django_project.category_app.repository import DjangoORMCategoryRepository

# Create your views here.

# pylint: disable=unused-argument


class CategoryViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        queries = ListCategoriesRequest()
        use_case = ListCategories(repository=DjangoORMCategoryRepository())
        categories = use_case.execute(request=queries)

        data = [
            {
                "id": str(category.id),
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active
            } for category in categories.data
        ]

        return Response(
            status=HTTP_200_OK,
            data=data
        )

    def retrieve(self, request: Request, pk=None) -> Response:  # route get by id
        try:
            category_id = UUID(pk)
        except ValueError:
            return Response(
                status=HTTP_400_BAD_REQUEST,
            )

        query = GetCategoryRequest(id=category_id)
        use_case = GetCategory(repository=DjangoORMCategoryRepository())

        try:
            category = use_case.execute(request=query)
        except CategoryNotFound:
            return Response(
                status=HTTP_404_NOT_FOUND,
                data={
                    "message": "Category not found"
                }
            )

        return Response(
            status=HTTP_200_OK,
            data={
                "id": str(category.id),
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active
            }
        )
