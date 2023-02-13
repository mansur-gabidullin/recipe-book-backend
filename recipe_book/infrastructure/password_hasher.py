from concurrent.futures import ThreadPoolExecutor, as_completed

from argon2 import PasswordHasher as Hasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash, HashingError


class PasswordHasher:
    def __init__(self):
        self._hasher = Hasher()

    async def hash(self, password: str) -> str:
        with ThreadPoolExecutor() as executor:
            (future,) = as_completed([executor.submit(lambda: self._hasher.hash(password))])
            try:
                return future.result()
            except HashingError as error:
                # todo: raise custom error
                raise error

    async def verify(self, hash_: str, password: str) -> bool:
        with ThreadPoolExecutor() as executor:
            future = next(as_completed([executor.submit(lambda: self._hasher.verify(hash_, password))]))
            try:
                return future.result()
            except (VerifyMismatchError, VerificationError, InvalidHash) as error:
                # todo: log error
                print(error)
                return False