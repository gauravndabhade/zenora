import typing
import datetime

import zenora
from zenora.base.factory import Factory as BaseFactory


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
        zenora.channels.PartialChannel
                Partial channel object since REST API may not always provide all data
                about channels.
        """
        return zenora.channels.GuildTextChannel(
            data=response
        )
