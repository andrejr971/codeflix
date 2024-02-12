
# import unittest
import uuid
import pytest

from src.core.genre.domain.genre import Genre


class TestGenre:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Genre()  # pylint: disable=no-value-for-parameter

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError,  match="name cannot be longer 255"):
            Genre(name="a" * 256)

    def test_created_genre_with_default_values(self):
        genre = Genre(name='Romance')
        assert genre.name == 'Romance'
        assert genre.is_active is True
        assert genre.id is not None
        assert isinstance(genre.id, uuid.UUID)
        assert genre.categories == set()

    def test_created_genre_with_provided_values(self):
        genre_id = uuid.uuid4()
        categories = {uuid.uuid4(), uuid.uuid4()}
        genre = Genre(
            name='Romance',
            is_active=False,
            id=genre_id,
            categories=categories
        )
        assert genre.name == 'Romance'
        assert genre.is_active is False
        assert genre.id == genre_id
        assert genre.categories == categories

    def test_cannot_create_genre_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Genre(name="")

    def test_method_repr(self):
        genre_id = uuid.uuid4()
        genre = Genre(
            name='Romance',
            id=genre_id
        )
        assert repr(genre) == f"<Genre Romance ({genre_id})>"


class TestUpdateStatusIsActive:
    def test_update_is_active_to_true(self):
        genre = Genre(
            name="Romance",
            is_active=False
        )
        genre.activate()

        assert genre.is_active is True

    def test_update_is_active_to_false(self):
        genre = Genre(
            name="Romance",
        )
        genre.desactivate()

        assert genre.is_active is False


class TestEquality:

    def test_when_genres_have_same_id_they_are_equals(self):
        common_id = uuid.uuid4()
        genre_1 = Genre(name="Romance", id=common_id)
        genre_2 = Genre(name="Action", id=common_id)

        assert genre_1 == genre_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        genre_1 = Genre(name="Romance", id=common_id)
        dummy = Dummy()
        dummy.id = common_id  # pylint: disable=attribute-defined-outside-init

        assert genre_1 != dummy


class TestChangeName:

    def test_change_name(self):
        genre = Genre(name="Romance")
        genre.change_name("Action")

        assert genre.name == "Action"

    def test_cannot_change_name_to_empty(self):
        genre = Genre(name="Romance")
        with pytest.raises(ValueError, match="name cannot be empty"):
            genre.change_name("")


class TestAddCaterory:

    def test_add_category(self):
        genre = Genre(name="Romance")
        category_id = uuid.uuid4()

        assert category_id not in genre.categories
        genre.add_category(category_id)
        assert category_id in genre.categories

    def test_add_multiple_categories(self):
        genre = Genre(name="Romance")
        category_1 = uuid.uuid4()
        category_2 = uuid.uuid4()

        assert category_1 not in genre.categories
        assert category_2 not in genre.categories
        genre.add_category(category_1)
        genre.add_category(category_2)
        assert category_1 in genre.categories
        assert category_2 in genre.categories


class TestRemoveCategory:

    def test_remove_category(self):
        category_id = uuid.uuid4()
        genre = Genre(name="Romance", categories={category_id})

        assert category_id in genre.categories
        genre.remove_category(category_id)
        assert category_id not in genre.categories
