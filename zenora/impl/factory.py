import typing
import datetime

from zenora.users import User
from zenora.base.factory import Factory as BaseFactory
from zenora.impl.mapper import ChannelMapper


class Factory(BaseFactory):
    def parse_channel(response: typing.Dict, app):
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

        return ChannelMapper.map(response, app)

    def parse_user(response: typing.Dict, app):
        return User(response, app)