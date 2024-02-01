from dataclasses import dataclass
from uuid import UUID
from src.core.category.domain.category_repository import CategoryRepository

# pylint: disable=line-too-long
from src.core.category.domain.category import Category
from src.core.category.domain.exceptions import InvalidCategoryData


@dataclass
class CreateCategoryRequest:
    name: str
    description: str = ""
    is_active: bool = True


@dataclass
class CreateCategoryResponse:
    id: UUID


class CreateCategory:
    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse:
        try:
            category = Category(
                name=request.name,
                description=request.description,
                is_active=request.is_active
            )
        except ValueError as error:
            # pylint: disable=raise-missing-from
            raise InvalidCategoryData(error)

        self.repository.save(category=category)

        return CreateCategoryResponse(id=category.id)


# def create_category(
#     repositoy: InMemoryCategoryRepository,
#     name: str,
#     description: str = "",
#     is_active: bool = True,
# ) -> UUID:
#     try:
#         category = Category(
#             name=name,
#             description=description,
#             is_active=is_active
#         )
#     except ValueError as error:
#         # pylint: disable=raise-missing-from
#         raise InvalidCategoryData(error)

#     repositoy.save(category=category)

#     return category.id
