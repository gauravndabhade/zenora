import typing
from zenora.channels import GuildTextChannel
from zenora.base.mapper import ChannelMapper as BaseChannelMapper


class ChannelMapper(BaseChannelMapper):

    def map(response) -> typing.Optional[GuildTextChannel]:
        """Implementation of the channel mapper.

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

        if int(response['type']) == 0:
            return GuildTextChannel(response)
