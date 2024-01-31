# from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

# Create your views here.

# pylint: disable=unused-argument


class CategoryViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        return Response(
            status=HTTP_200_OK,
            data=[
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
        )
