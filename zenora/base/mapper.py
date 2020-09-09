import abc
import typing
from zenora.channels import GuildTextChannel


class ChannelMapper(abc.ABC):

    @abc.abstractmethod
    def map(self, response) -> typing.Optional[GuildTextChannel]:
        """Interface of channel mapper

        Maps channel response to object according to channel type.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora text channel model consisting of channel data.
        """
