from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional


@dataclass
class PCOToken:
    token_type: str = "bearer"
    access_token: Optional[str] = None
    expires_in: Optional[int] = -1
    refresh_token: Optional[str] = None
    scope: Optional[List[str]] = None
    created_at: Optional[int] = None
    expires_at: Optional[Decimal] = None
