import typing
import datetime

from zenora.users import User
from zenora.messages import Message
from zenora.base.factory import Factory as BaseFactory
from zenora.impl.mapper import ChannelMapper


class Factory(BaseFactory):
    def parse_channel(response: typing.Dict, app):
        """Parses response data from Dicord API into channel objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Zenora REST API object

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        return ChannelMapper.map(response, app)

    def parse_user(response: typing.Dict, app):
        """Parses response data from Dicord API into user objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the user

        Returns
        -------
        zenora.users.User
                Zenora user object
        """
        return User(response, app)

    def parse_message(response: typing.Dict, app) -> typing.Any:
        """Parses response data from Dicord API into message object

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        snowflake: int
                Snowflake ID of the message

        Returns
        -------
        zenora.messages.Message
                Zenora message object

        """
        return Message(response, app)
