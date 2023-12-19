from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from datetime import datetime
from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name="Movie")
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description,  None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()
        category = Category(
            name='movie 2',
            description='some description',
            is_active=False,
            created_at=created_at
        )
        self.assertEqual(category.name, 'movie 2')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        categoryOne = Category(name="Movie 1")
        categoryTwo = Category(name="Movie 2")
        self.assertNotEqual(
            categoryOne.created_at,
            categoryTwo.created_at
        )
        self.assertNotEqual(
            categoryOne.created_at.timestamp(),
            categoryTwo.created_at.timestamp()
        )

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            category = Category(name="Movie 1")
            category.name = 'Movie 2'

    def test_update(self):
        category = Category(name='Movie')
        category.update('Documentary', 'some description')
        self.assertEqual(category.name, 'Documentary')
        self.assertEqual(category.description, 'some description')

    def test_activate(self):
        # with patch.object(Category, 'validate'):
        category = Category(name='Movie', is_active=False)
        category.activate()
        self.assertTrue(category.is_active)

    def test_deactivate(self):
        # with patch.object(Category, 'validate'):
        category = Category(name='Movie')
        category.deactivate()
        self.assertFalse(category.is_active)
