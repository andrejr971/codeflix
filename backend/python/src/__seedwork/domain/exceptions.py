from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from __seedwork.domain.validators import ErrorFields


class InvalidUuidException(Exception):
    def __init__(self, error='ID must be a valid UUID') -> None:
        super().__init__(error)


class ValidationException(Exception):
    def __init__(self, error: str) -> None:
        super().__init__(error)


class EntityValidationException(Exception):
    error: 'ErrorFields'

    def __init__(self, error: 'ErrorFields') -> None:
        self.error = error
        super().__init__('Entity Validation Error')


class NotFoundException(Exception):
    def __init__(self, error='Not found') -> None:
        super().__init__(error)
