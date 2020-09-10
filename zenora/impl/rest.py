import typing
import zenora
from zenora.base.rest import RESTAPI as REST
from zenora.impl.factory import Factory as model_factory
from zenora.impl.query import Query


class RESTAPI(REST):

    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str) -> None:
        self.token = token
        self.token_type = token_type

    def get_channel(self, snowflake: int) -> typing.Any:
        """Fetch Dicord Channel

        This has to be the channel snowflake ID


        Parameters
        ----------

        snowflake: int
                The channel ID of the specific channel you want to fetch

        Returns
        -------
        zenora.channels.GuildTextChannel
                Zenora guild text channel object

        zenora.channels.GuildVoiceChannel
                Zenora guild voice channel object

        zenora.channels.DMTextChannel
                Zenora DM text channel object
        """
        response = Query(self.token, self.token_type).channel(snowflake)
        return model_factory.parse_channel(response)
