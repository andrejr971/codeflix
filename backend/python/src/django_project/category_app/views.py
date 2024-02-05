# from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from core.category.application.usecases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.usecases.get_category import GetCategory, GetCategoryRequest
from src.core.category.application.usecases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.application.usecases.delete_category import DeleteCategory, DeleteCategoryRequest

from src.core.category.application.usecases.list_categories import ListCategories, ListCategoriesRequest
from src.core.category.domain.exceptions import CategoryNotFound
from src.django_project.category_app.repository import DjangoORMCategoryRepository
from src.django_project.category_app.serializers import CreateCategoryRequestSerializer, CreateCategoryResponseSerializer, DeleteCategoryRequestSerializer, ListCategoryResponseSerializer, RetrieveCategoryRequestSerializer, RetrieveCategoryResponseSerializer, UpdateCategoryRequestSerializer

# Create your views here.

# pylint: disable=unused-argument


class CategoryViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        queries = ListCategoriesRequest()
        use_case = ListCategories(repository=DjangoORMCategoryRepository())
        response = use_case.execute(request=queries)

        serializers = ListCategoryResponseSerializer(instance=response)

        return Response(
            status=HTTP_200_OK,
            data=serializers.data
        )

    def retrieve(self, request: Request, pk=None) -> Response:  # route get by id
        serializers_id = RetrieveCategoryRequestSerializer(data={"id": pk})
        serializers_id.is_valid(raise_exception=True)

        query = GetCategoryRequest(id=serializers_id.validated_data["id"])
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

        serializers = RetrieveCategoryResponseSerializer(instance=category)

        return Response(
            status=HTTP_200_OK,
            data=serializers.data
        )

    def create(self, request: Request) -> Response:
        serialize = CreateCategoryRequestSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)

        data = CreateCategoryRequest(**serialize.validated_data)
        use_case = CreateCategory(repository=DjangoORMCategoryRepository())

        category = use_case.execute(request=data)

        return Response(
            status=HTTP_201_CREATED,
            data=CreateCategoryResponseSerializer(instance=category).data
        )

    def update(self, request: Request, pk=None) -> Response:
        serializer = UpdateCategoryRequestSerializer(
            data={
                "id": pk,
                **request.data
            }
        )
        serializer.is_valid(raise_exception=True)

        data = UpdateCategoryRequest(**serializer.validated_data)
        use_case = UpdateCategory(repository=DjangoORMCategoryRepository())

        try:
            use_case.execute(request=data)
        except CategoryNotFound:
            return Response(
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def destroy(self, request: Request, pk=None) -> Response:
        serializer = DeleteCategoryRequestSerializer(
            data={
                "id": pk,
            }
        )
        serializer.is_valid(raise_exception=True)

        data = DeleteCategoryRequest(**serializer.validated_data)
        use_case = DeleteCategory(repository=DjangoORMCategoryRepository())

        try:
            use_case.execute(request=data)
        except CategoryNotFound:
            return Response(
                status=HTTP_404_NOT_FOUND,
            )

        return Response(
            status=HTTP_204_NO_CONTENT,
        )
