from dataclasses import dataclass
from typing import Optional


@dataclass
class PCOToken:
    token_type: str = "bearer"
    access_token: Optional[str] = None
    expires_in: Optional[int] = -1
    refresh_token: Optional[str] = None
