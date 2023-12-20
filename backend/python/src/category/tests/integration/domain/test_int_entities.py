import unittest
from __seedwork.domain.exceptions import ValidationException

from category.domain.entities import Category


class TestCateogryIntegration(unittest.TestCase):

    def test_create_with_invalida_cases_for_name_props(self):
        with self.assertRaises(ValidationException) as error:
            Category(name=None)
        self.assertEqual('The name is required', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            Category(name='')
        self.assertEqual('The name is required', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            Category(name=5)
        self.assertEqual('The name must be a string', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            Category(name='t' * 256)
        self.assertEqual(
            'The name must be less than 255 characters',
            error.exception.args[0]
        )

    def test_create_with_invalida_cases_for_description_props(self):
        with self.assertRaises(ValidationException) as error:
            Category(name='Movie', description={})
        self.assertEqual(
            'The description must be a string',
            error.exception.args[0]
        )

    def test_create_with_invalida_cases_for_is_active_props(self):
        with self.assertRaises(ValidationException) as error:
            Category(name='Movie', is_active=5)
        self.assertEqual(
            'The is_active must be a boolean',
            error.exception.args[0]
        )

    def test_create_with_valide_cases(self):
        try:
            Category(name="Movie")
            Category(
                name='Movie',
                description='Movie description',
                is_active=True
            )
            Category(
                name='Movie',
                is_active=True
            )
            Category(
                name='Movie',
                is_active=False
            )
            Category(
                name='Movie',
                description=None,
                is_active=True
            )
            Category(
                name='Movie',
                description="",
                is_active=True
            )
            Category(
                name='Movie',
                description="",
                is_active=False
            )
        except ValidationException as error:
            self.fail(f'Some prop is not valid: Error: {error.args[0]}')

    def test_update_with_invalida_cases_for_name_props(self):
        category = Category(name='Movie')
        with self.assertRaises(ValidationException) as error:
            category.update(name=None)
        self.assertEqual('The name is required', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            category.update(name='')
        self.assertEqual('The name is required', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            category.update(name=5)
        self.assertEqual('The name must be a string', error.exception.args[0])

        with self.assertRaises(ValidationException) as error:
            category.update(name='t' * 256)
        self.assertEqual(
            'The name must be less than 255 characters',
            error.exception.args[0]
        )

    def test_update_with_invalida_cases_for_description_props(self):
        category = Category(name='Movie', description='Movie description')
        with self.assertRaises(ValidationException) as error:
            category.update(name='Movie', description={})
        self.assertEqual(
            'The description must be a string',
            error.exception.args[0]
        )

    def test_update_with_valide_cases(self):
        category = Category(name="Movie")
        try:
            category.update(
                name='Movie',
                description='Movie description',
            )
            category.update(
                name='Movie',
                description=None
            )
            category.update(
                name='Movie',
                description="",
            )
        except ValidationException as error:
            self.fail(f'Some prop is not valid: Error: {error.args[0]}')
