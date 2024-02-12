
from src.core.category.domain.category import Category
from src.core.category.infra.repositories.in_memory_category_repository import (
    InMemoryCategoryRepository
)
from src.core.genre.application.usecases.update_genre import UpdateGenre
from src.core.genre.domain.genre import Genre
from src.core.genre.infra.repositories.in_memory_genre_repository import InMemoryGenreRepository


class TestUpdateGenre:
    def test_can_update_genre_name(self):
        genre = Genre(
            name="Drama",
        )
        repository = InMemoryGenreRepository()
        repository.save(genre=genre)
        category_repository = InMemoryCategoryRepository()

        use_case = UpdateGenre(
            repository=repository,
            category_repository=category_repository
        )
        request = UpdateGenre.Request(
            id=genre.id,
            name="Action",
        )
        use_case.execute(request=request)

        updated_category = repository.get_by_id(genre.id)
        assert updated_category.name == "Action"

    def test_can_update_genre_categories(self):
        movie = Category(
            name="Movie",
            description="some description",
        )
        serie = Category(
            name="Serie",
            description="some description",
        )
        genre = Genre(
            name="Drama",
        )
        repository = InMemoryGenreRepository()
        repository.save(genre=genre)
        category_repository = InMemoryCategoryRepository(
            categories=[movie, serie]
        )

        use_case = UpdateGenre(
            repository=repository,
            category_repository=category_repository
        )
        request = UpdateGenre.Request(
            id=genre.id,
            categories={movie.id, serie.id},
        )
        use_case.execute(request=request)

        updated_category = repository.get_by_id(genre.id)
        assert updated_category.categories == {movie.id, serie.id}
