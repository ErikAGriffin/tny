from redis import Redis
from config import DevelopmentConfig

class RedisClient:

    __url_prefix = "url_hash:"

    def __init__(self, config=DevelopmentConfig):
        self._client = Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=0,
            decode_responses=True
        )

    def set_url(self, url_hash, url):
        key = f"{self.__url_prefix}{url_hash}"
        self._client.set(f"{self.__url_prefix}{url_hash}", url)

    def get_url(self, url_hash):
        key = f"{self.__url_prefix}{url_hash}"
        return self._client.get(f"{self.__url_prefix}{url_hash}")
