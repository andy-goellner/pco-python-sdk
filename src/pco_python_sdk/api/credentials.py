from dataclasses import dataclass
from typing import Callable, Optional

from pco_python_sdk.api.pco_token import PCOToken


@dataclass
class Credentials:
    client_id: str
    client_secret: str
    access_code: Optional[str] = None
    pco_token: Optional[PCOToken] = None
    token_updater: Optional[Callable[..., None]] = None
