from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import uuid


@dataclass(kw_only=True, frozen=True)  # init, repr, eq
class Category:

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
    )

# def __init__(self, name: str, description: str, is_active: bool, created_at: datetime) -> None: # constructor
#   self.name = name
#   self.description = description
#   self.is_active = is_active
#   self.created_at = created_at
