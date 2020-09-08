
import typing
import abc


class RESTAPI(abc.ABC):
    """Base interface for the implementation of the REST API."""

    __slots__ = ['token', 'token_type']

    def __init__(self, token: str, token_type: str) -> None:
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def get_channel(self, snowflake: int) -> None:
        """Fetch channels

        This has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch
        """
