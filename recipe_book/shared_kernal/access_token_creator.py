from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from datetime import timedelta, datetime, UTC

from jose import jwt, JWTError
from jose.exceptions import JWTClaimsError, ExpiredSignatureError

from .interfaces.access_token_creator import ITokenCreator


class TokenCreator(ITokenCreator):
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        csrf_expire_minutes: int,
        access_expire_minutes: int,
        refresh_expire_days: int,
    ):
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._csrf_expires_delta = timedelta(minutes=csrf_expire_minutes)
        self._access_expires_delta = timedelta(minutes=access_expire_minutes)
        self._refresh_expires_delta = timedelta(days=refresh_expire_days)
        self._encoder = jwt

    async def create(self, data: dict, expires_delta: timedelta) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": datetime.now(UTC) + expires_delta})

        with ThreadPoolExecutor() as executor:
            future: Future
            [future] = as_completed(
                [executor.submit(lambda: self._encoder.encode(to_encode, self._secret_key, algorithm=self._algorithm))]
            )
            try:
                return future.result()
            except JWTError as error:
                # todo: raise custom error
                raise error

    async def create_csrf_token(self, data: dict) -> str:
        return await self.create(data, self._csrf_expires_delta)

    async def create_refresh_token(self, data: dict) -> str:
        return await self.create(data, self._refresh_expires_delta)

    async def create_access_token(self, data: dict) -> str:
        return await self.create(data, self._access_expires_delta)

    async def read(self, token: str) -> dict:
        with ThreadPoolExecutor() as executor:
            future: Future
            [future] = as_completed(
                [executor.submit(lambda: self._encoder.decode(token, self._secret_key, algorithms=[self._algorithm]))]
            )
            try:
                return future.result()
            except (JWTError, ExpiredSignatureError, JWTClaimsError) as error:
                # todo: raise custom error
                raise error
