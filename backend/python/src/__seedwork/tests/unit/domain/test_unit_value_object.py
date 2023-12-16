from dataclasses import FrozenInstanceError, is_dataclass
import unittest
from unittest.mock import patch
import uuid

from __seedwork.domain.value_object import UniqueEntityId
from __seedwork.domain.exceptions import InvalidUuidException


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')

            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID'
            )

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            entity_id = UniqueEntityId('f1524b40-aa63-4813-b863-7e2c860eeba1')
            mock_validate.assert_called_once()
            self.assertEqual(
                entity_id.id, 'f1524b40-aa63-4813-b863-7e2c860eeba1'
            )

        uuid_value = uuid.uuid4()
        entity_id = UniqueEntityId(uuid_value)
        self.assertEqual(
            entity_id.id, str(uuid_value)
        )

    def test_generate_id_when_no_passed_id_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        ) as mock_validate:
            entity_id = UniqueEntityId()
            self.assertTrue(entity_id.id)
            mock_validate.assert_called_once()

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError) as frozen_error:
            entity_id = UniqueEntityId()
            entity_id.id = 'fake id'

        self.assertEqual(
            frozen_error.exception.args[0], "cannot assign to field 'id'"
        )

    def test_convert_to_str(self):
        entity_id = UniqueEntityId()
        self.assertEqual(entity_id.id, str(entity_id))
