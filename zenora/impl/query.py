import abc
import typing


class Query(abc.ABC):
    __slots__ = ['token', 'token_type']

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def channel(self, snonwflake: int) -> typing.Dict:
        """Interface for the REST API query to get channels.

        Parameters:
        snowflask: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
