from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import timedelta, datetime

from jose import jwt, JWTError
from jose.exceptions import JWTClaimsError, ExpiredSignatureError

from application_core.bounded_contexts.users.ports.secondary import IAccessTokenCreator


class AccessTokenCreator(IAccessTokenCreator):
    def __init__(self, secret_key: str, algorithm: str, expires_minutes: int):
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._expires_delta = timedelta(minutes=expires_minutes)
        self._encoder = jwt

    async def create(self, data: dict) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": datetime.utcnow() + self._expires_delta})

        with ThreadPoolExecutor() as executor:
            (future,) = as_completed(
                [executor.submit(lambda: self._encoder.encode(to_encode, self._secret_key, algorithm=self._algorithm))]
            )
            try:
                return future.result()
            except JWTError as error:
                # todo: raise custom error
                raise error

    async def read(self, token: str) -> dict:
        with ThreadPoolExecutor() as executor:
            (future,) = as_completed(
                [executor.submit(lambda: self._encoder.decode(token, self._secret_key, algorithms=[self._algorithm]))]
            )
            try:
                return future.result()
            except (JWTError, ExpiredSignatureError, JWTClaimsError) as error:
                # todo: raise custom error
                raise error
