import abc
import typing


class Query(abc.ABC):
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def channel(self, snonwflake: int) -> typing.Dict:
        """Interface for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def user(self, snowflake: int) -> typing.Dict:
        """Interface for the REST API query to get user.

        Parameters:
        snowflake: int
                The ID of a Discord User

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def current_user(self) -> typing.Dict:
        """Interface for the REST API query to get current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def modify_me(self, args: dict) -> typing.Dict:
        """Interface for the REST API query to modify current user.

        Returns:
        typing.Dict:
                A dictionary object that will be used to parse the data
                into objects
        """

    @abc.abstractmethod
    def modify_channel(self, channel_id: int, args: typing.Dict):
        """Interface for the REST API query to modify guild channel.

        Returns:
        channel_id: int
                The snowflake ID of the channel.
        typing.Dict:
                A dictionary object that will be used to parse the data
                into objects

        """

    @abc.abstractmethod
    def delete_channel(self, channel_id):
        """Interface for the REST API query to delete guild channel.

        Returns:
        channel_id: int
                The snowflake ID of the channel.

        """

    @abc.abstractmethod
    def leave_guild(self, snowflake: int):
        """Interface for the REST API query to leave a guild.

        Returns:
        code: int
            Code for response status. Will return 204 on success
        """

    @abc.abstractmethod
    def current_user_dms(self) -> typing.Dict:
        """Interface for the REST API query to fetch current user's DMs list

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def create_dm(self, recipient_id: int) -> typing.Dict:
        """Interface for the REST API query to create a DM with a specific user according to ID

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
