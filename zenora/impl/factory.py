import typing
import datetime

import zenora
from zenora.base.factory import Factory as BaseFactory
from zenora.impl.mapper import ChannelMapper


class Factory(BaseFactory):
    def parse_channel(response: typing.Dict):
        """Parses response data from Dicord API into channel objects

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
        """

        return ChannelMapper.map(response)