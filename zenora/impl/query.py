import typing
from zenora.utils.helpers import fetch
from zenora.utils.endpoints import *


class Query:
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    def channel(self, snowflake: int) -> typing.Dict:
        """Implementation for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
        data = fetch(
            BASE_URL + FETCH_CHANNEL.format(snowflake),
            headers={"Authorization": f"{self.token_type} {self.token}"},
        )
        return data
