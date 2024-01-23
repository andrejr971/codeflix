
# import unittest
import uuid
import pytest

from category import Category


class TestCategory:

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()  # pylint: disable=no-value-for-parameter

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError,  match="name cannot be longer 255"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category('movie')
        assert isinstance(category.id, uuid.UUID)

    def test_created_category_with_default_values(self):
        category = Category(name='movie')
        assert category.name == 'movie'
        assert category.description == ''
        assert category.is_active is True

    def test_category_is_created_as_active_by_default(self):
        category = Category(name='movie')
        assert category.is_active is True

    def test_create_category_with_params(self):
        category_id = uuid.uuid4()
        category = Category(
            name='movie',
            id=category_id,
            description='some description',
            is_active=False
        )
        assert category.name == 'movie'
        assert category.id == category_id
        assert category.description == 'some description'
        assert category.is_active is False

    def test_method_str(self):
        category_id = uuid.uuid4()
        category = Category(
            name='movie',
            id=category_id
        )
        assert str(category) == f"movie -  ({category_id})"

    def test_method_repr(self):
        category_id = uuid.uuid4()
        category = Category(
            name='movie',
            id=category_id
        )
        assert repr(category) == f"<Category movie ({category_id})>"

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot empty"):
            Category(name="")


class TestUpdateCategory:

    def test_update_with_name_and_description(self):
        category = Category(name="Serie", description="some description")
        category.update(name="Serie 1", description="")

        assert category.name == "Serie 1"
        assert category.description == ""

    def test_update_with_invalid_name_raise_exception(self):
        category = Category(name="Serie", description="some description")

        with pytest.raises(ValueError,  match="name cannot be longer 255"):
            category.update(name="a" * 256, description="")

    def test_cannot_update_category_with_empty_name(self):
        category = Category(name="Serie", description="some description")

        with pytest.raises(ValueError, match="name cannot empty"):
            category.update(name="" * 256, description="")


class TestUpdateStatusIsActive:
    def test_update_is_active_to_true(self):
        category = Category(
            name="Serie",
            description="some description",
            is_active=False
        )
        category.activate()

        assert category.is_active is True

    def test_update_is_active_to_false(self):
        category = Category(
            name="Serie",
            description="some description"
        )
        category.desactivate()

        assert category.is_active is False


class TestEquality:

    def test_when_categories_have_same_id_they_are_equals(self):
        common_id = uuid.uuid4()
        category_1 = Category(name="Film", id=common_id)
        category_2 = Category(name="Film", id=common_id)

        assert category_1 == category_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        category_1 = Category(name="Film", id=common_id)
        dummy = Dummy()
        dummy.id = common_id  # pylint: disable=attribute-defined-outside-init

        assert category_1 != dummy

# if __name__ == "__main__":
#     unittest.main()
