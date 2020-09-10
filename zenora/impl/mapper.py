import typing
from zenora.channels import *
from zenora.base.mapper import ChannelMapper as BaseChannelMapper
from zenora.errors import MissingAccess


class ChannelMapper(BaseChannelMapper):
    def map(response) -> typing.Any:
        """Implementation of the channel mapper.

        Maps channel response to object according to channel type.

        Parameters
        ----------
        response: typing.Dict
                API response from Discord

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        if "code" in response and response["code"] == 50001:
            raise MissingAccess("You don't have access to this channel")

        if response["type"] == 0:
            return GuildTextChannel(response)
        elif response["type"] == 1:
            return DMTextChannel(response)
        elif response["type"] == 2:
            return GuildVoiceChannel(response)
