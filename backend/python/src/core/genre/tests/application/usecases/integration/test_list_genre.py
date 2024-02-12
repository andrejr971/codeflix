from src.core.genre.application.usecases.list_genre import ListGenre, ResponseListGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.repositories.in_memory_genre_repository import (
    InMemoryGenreRepository
)
from src.core.category.infra.repositories.in_memory_category_repository import (
    InMemoryCategoryRepository
)
from src.core.category.domain.category import Category


class TestListGenre:

    def test_list_genre_with_associated_categories(
        self,
    ):
        category_repository = InMemoryCategoryRepository()
        genre_repository = InMemoryGenreRepository()

        cat_1 = Category(
            name="Category 1",
            description="Category 1 description"
        )
        category_repository.save(cat_1)

        cat_2 = Category(
            name="Category 2",
            description="Category 2 description"
        )
        category_repository.save(cat_2)

        genre_drama = Genre(
            name="Drama",
            categories={cat_1.id, cat_2.id},
        )
        genre_repository.save(genre_drama)

        genre_romance = Genre(name="Romance")
        genre_repository.save(genre_romance)

        use_case = ListGenre(repository=genre_repository)
        use_case = ListGenre(
            repository=genre_repository
        )
        response = use_case.execute(ListGenre.Request())

        assert len(response.data) == 2
        assert response == ListGenre.Response(
            data=[
                ResponseListGenre(
                    id=genre_drama.id,
                    name="Drama",
                    categories={cat_1.id, cat_2.id},
                    is_active=True,
                ),
                ResponseListGenre(
                    id=genre_romance.id,
                    name="Romance",
                    categories=set(),
                    is_active=True,
                )
            ]
        )
