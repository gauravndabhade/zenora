import abc
import typing
import zenora


class Factory(abc.ABC):
    @abc.abstractmethod
    def parse_channel(response: typing.Dict, app) -> typing.Any:
        """Parses response data from Dicord API into channel objects

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Instance of the RESTAPI

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
    def parse_user(response: typing.Dict, app) -> typing.Any:
        """Interface of data parser for user object

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Instance of the RESTAPI

        Returns
        -------
        zenora.users.User
                Zenora user object

        """

    @abc.abstractmethod
    def parse_message(response: typing.Dict, app) -> typing.Any:
        """Interface of data parser for message object

        Parameters
        ----------
        response: typing.Dict
                Discord API response as dictionary/JSON
        app: zenora.RESTAPI
                Instance of the RESTAPI

        Returns
        -------
        zenora.messages.Message
                Zenora message object

        """
