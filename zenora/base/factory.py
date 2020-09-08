import abc
import typing
import attr
import zenora


class Factory(abc.ABC):
    @abc.abstractmethod
    def parse_channel(self, response: typing.Dict, snowflake: int):
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
                Partial channel object since REST API may not always provide all data
                about channels.  
        """
