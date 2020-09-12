import abc
import typing
import zenora


class Factory(abc.ABC):
    @abc.abstractmethod
    def parse_channel(self, response: typing.Dict, snowflake: int) -> typing.Any:
        """Interface of data parser for channel object

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the channel

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """

    @abc.abstractmethod
    def parse_user(self, response: typing.Dict, snowflake: int) -> typing.Any:
        """Interface of data parser for user object

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the channel

        Returns
        -------
        zenora.users.User
                Zenora partial user object

        """
