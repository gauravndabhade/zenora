import typing
import abc


class RESTAPI(abc.ABC):
    """Base interface for the implementation of the REST API."""

    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str) -> None:
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def get_text_channel(self, snowflake: int) -> None:
        """Fetch guild text channel

        This has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object
        """

    @abc.abstractmethod
    def get_dm_channel(self, snowflake: int) -> None:
        """Fetch guild DM channel

        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch

        Returns
        -------
        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """

    @abc.abstractmethod
    def get_voice_channel(self, snowflake: int) -> None:
        """Fetch guild voice channel

        :param snowflake: [description]
        :type snowflake: int

        Returns
        -------
        zenora.channels.GuildVoiceChannel
            Zenora guild voice channel object
        """
