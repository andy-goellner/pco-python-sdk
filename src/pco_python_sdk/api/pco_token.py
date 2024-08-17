from dataclasses import dataclass
from typing import Optional


@dataclass
class PCOToken:
    created_at: Optional[int] = None
    expires_in: Optional[int] = None
    refresh_token: Optional[str] = None
